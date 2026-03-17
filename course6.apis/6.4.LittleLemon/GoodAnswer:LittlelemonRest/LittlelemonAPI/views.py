from django.shortcuts import render,get_object_or_404
from django.db import transaction
from .models import MenuItem, User, Group, Cart, Order, OrderItem, Category
from .serializers import MenuItemSerializer, UserSerializer, CartSerializer, OrderSerializer, OrderItemSerializer, CategorySerializer
from rest_framework import generics, permissions,status, serializers
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from datetime import date
# Create your views here.

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='Manager').exists()


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':        
            return [permissions.AllowAny()]
        
        return [IsManager()]


### Allows get and post request to add Menu Item 
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all() # tells Django which records from the db should be involved 
    serializer_class = MenuItemSerializer # for get request, it takes the queryset results and converts into a simple JSON list

    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['price']
    filterset_fields = ['category']
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_permissions(self):
        if self.request.method == 'GET':        
            return [permissions.AllowAny()]
        
        return [IsManager()]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'title'

    def get_permissions(self):
        if self.request.method == 'GET':        
            return [permissions.AllowAny()]
        
        return [IsManager()]
    
 
class ManagersViewSet(generics.ListCreateAPIView):
    serializer_class = UserSerializer 
    permission_classes = [IsManager]

    def get_queryset(self):
        user_group_name = self.kwargs.get('group_name').capitalize()
        return User.objects.filter(groups__name=user_group_name)

    # Assigns user in request body to the group defined in the url 
    def create(self, request, *args, **kwargs):

        user_group_name = self.kwargs.get('group_name').capitalize()
        
        if user_group_name == 'Delivery-crew':
            user_group_name = 'Delivery crew'
        

        target_group = Group.objects.get(name=user_group_name)
        username = request.data.get('username')

        if username: 
            user = User.objects.get(username=username)
            user.groups.add(target_group) # revise the group column in the user to the target group
            return Response({"message":"User assigned"}, status=status.HTTP_201_CREATED)

        return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)
    
class ManagerViewSetSingleUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsManager]

    def destroy(self,request, *args, **kwargs):
        # identify group from url
        user_group_name = self.kwargs.get('group_name').capitalize()

        if user_group_name == 'Delivery-crew':
            user_group_name = 'Delivery crew'

        target_group = get_object_or_404(Group, name=user_group_name)
        # identify from {userid}. It will automatically take it as a primary key 
        user = self.get_object()

        # check if the target_group object is in the join table that connects Users to Groups 
        if target_group in user.groups.all():
            user.groups.remove(target_group)
            return Response({"message":f"User removed from {user_group_name}"}, status=status.HTTP_200_OK)
        
        raise serializers.ValidationError({"detail": "User was not in this group"})


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user) # self.request.user holds the entire user object of the person logged in
    
    def perform_create(self, serializer): # perform_create is used to handle validated Serializer object only

        item = serializer.validated_data.get('menuitem') # validated_data is preferred over self.request.data.get('menuitem') because serializer contains fields defined in serializer

        quantity = serializer.validated_data.get('quantity')

        unit_price = item.price
        total_price = quantity*unit_price

        serializer.save(user = self.request.user, unit_price = unit_price, price = total_price)

class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        elif user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew = user)  # check that the userid has delivery crew in its group column and return the orders that have the user id in its delivery_crew column
        
        return Order.objects.filter(user = user)
    
    def perform_create(self, serializer):
        
        user = self.request.user
        cart_items = Cart.objects.filter(user = user)

        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty.")
        
        order_total = sum(item.price for item in cart_items)
        
        with transaction.atomic():

            # create a new row in the Order model with the user and order total info
            order = serializer.save(
                user = user,
                total = order_total,
                date = date.today()
            )

            order_items = []
            for item in cart_items:
                order_items.append(
                    OrderItem(
                        order = order,
                        menuitem = item.menuitem,
                        quantity = item.quantity,
                        unit_price = item.unit_price,
                        price = item.unit_price
                    )
                )
            
            OrderItem.objects.bulk_create(order_items)

            # remove the specific entries in the Cart Model also 
            cart_items.delete()


class OrderItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        order_id = self.kwargs.get('pk')
        
        if user.groups.filter(name='Manager').exists():
            return Order.objects.filter(id=order_id)
        
        if user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(id=order_id, delivery_crew=user)
        
        if Order.objects.filter(id=order_id, user=user).exists():
            return Order.objects.filter(id=order_id)
    
    def perform_destroy(self,instance):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            instance.delete()
        else: 
            raise PermissionDenied("Only managers can delete orders.")
        
    def perform_update(self, serializer):
        user = self.request.user
        instance = self.get_object() # The current Order in the database

        if user.groups.filter(name='Manager').exists():
            
            if 'delivery_crew' in serializer.validated_data:
                instance.delivery_crew = serializer.validated_data['delivery_crew'] 
        
            instance.status = serializer.validated_data.get('status', instance.status)
            instance.save(update_fields =['delivery_crew', 'status'])
            
        elif instance.delivery_crew == user : 
            instance.status = serializer.validated_data.get('status', instance.status)
            instance.save(update_fields=['status'])
            # serializer.save(status=serializer.validated_data.get('status')) # use this if we want to response to immediately reflect the change because the response load 
        else:
            raise PermissionDenied("You do not have permission to update this order.")
        
        
