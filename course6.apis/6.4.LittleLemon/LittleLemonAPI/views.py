from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import Group, User

from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    CartSerializer,
    OrderSerializer,
    UserSerializer,
)


class IsManagerUser(BasePermission):
    """Only superuser or users in the Manager group."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_superuser
            or request.user.groups.filter(name="Manager").exists()
        )


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        permission_class = []
        if self.request.method != 'GET':
            permission_class = [IsAuthenticated]

        return [permission() for permission in permission_class]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ['category__title']
    ordering_fields = ['price', 'inventory']

    def get_permissions(self):
        permission_class = []
        if self.request.method != 'GET':
            permission_class = [IsAuthenticated]

        return [permission() for permission in permission_class]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.all().filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        Cart.objects.filter(user=self.request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        elif self.request.user.groups.count() == 0:  # normal customer - no group
            return Order.objects.all().filter(user=self.request.user)
        elif self.request.user.groups.filter(name="Delivery Crew").exists():  # delivery crew
            return Order.objects.all().filter(
                delivery_crew=self.request.user
            )  # only show oreders assigned to him
        else:  # delivery crew or manager
            return Order.objects.all()
        
    def create(self, request, *args, **kwargs):
        menuitem_count = Cart.objects.filter(user=self.request.user).count()
        if menuitem_count == 0:
            return Response(
                {"message": "no item in cart"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = request.data.copy()
        total = self.get_total_price(self.request.user)
        data["total"] = total
        data["user"] = self.request.user.id
        data["date"] = timezone.now().date()
        order_serializer = OrderSerializer(data=data)
        if not order_serializer.is_valid():
            return Response(
                order_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        order = order_serializer.save()

        items = Cart.objects.filter(user=self.request.user).values()

        for item in items:
            OrderItem.objects.create(
                order=order,
                menuitem_id=item["menuitem_id"],
                quantity=item["quantity"],
                unit_price=item["unit_price"],
                price=item["price"],
            )

        Cart.objects.filter(user=self.request.user).delete()

        return Response(
            order_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def get_total_price(self, user):
        total = sum(
            item["price"]
            for item in Cart.objects.filter(user=user).values("price")
        )
        return total

class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        if self.request.user.groups.count() == 0:
            return Response(
                {"detail": "Customers cannot update orders."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

class GroupViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]

    def list(self, request):
        users = User.objects.all().filter(groups__name="Manager")
        items = UserSerializer(users, many=True)
        return Response(items.data)

    def create(self, request):
        user = get_object_or_404(User, username=request.data["username"])
        managers = Group.objects.get(name="Manager")
        managers.user_set.add(user)
        return Response({"message": "user added to the manager group"}, 200)

    def destroy(self, request):
        user = get_object_or_404(User, username=request.data["username"])
        managers = Group.objects.get(name="Manager")
        managers.user_set.remove(user)
        return Response({"message": "user removed from the manager group"}, 200)

class SingleManagerViewSet(viewsets.ViewSet):
    """Only for manager role: remove a user from the manager group by user id (pk)."""

    permission_classes = [IsAuthenticated, IsManagerUser]

    def list(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        if not user.groups.filter(name="Manager").exists():
            return Response({"message": "user not in manager group"}, status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = User.objects.all().filter(groups__name="Manager").get(pk=pk)
        managers = Group.objects.get(name="Manager")
        managers.user_set.remove(user)
        return Response(
            {"message": "user removed from the manager group"},
            status=status.HTTP_200_OK,
        )

class DeliveryCrewViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        users = User.objects.all().filter(groups__name="Delivery Crew")
        items = UserSerializer(users, many=True)
        return Response(items.data)

    def create(self, request):
        # only for super admin and managers
        if self.request.user.is_superuser == False:
            if self.request.user.groups.filter(name="Manager").exists() == False:
                return Response({"message": "forbidden"}, status.HTTP_403_FORBIDDEN)

        user = get_object_or_404(User, username=request.data["username"])
        dc = Group.objects.get(name="Delivery Crew")
        dc.user_set.add(user)
        return Response({"message": "user added to the delivery crew group"}, 200)

    def destroy(self, request):
        # only for super admin and managers
        if self.request.user.is_superuser == False:
            if self.request.user.groups.filter(name="Manager").exists() == False:
                return Response({"message": "forbidden"}, status.HTTP_403_FORBIDDEN)
        user = get_object_or_404(User, username=request.data["username"])
        dc = Group.objects.get(name="Delivery Crew")
        dc.user_set.remove(user)
        return Response({"message": "user removed from the delivery crew group"}, 200)


class SingleDeliveryCrewViewSet(viewsets.ViewSet):
    """Only for manager role: get or remove a user from the delivery crew group by user id (pk)."""

    permission_classes = [IsAuthenticated, IsManagerUser]

    def list(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        if not user.groups.filter(name="Delivery Crew").exists():
            return Response({"message": "user not in delivery crew group"}, status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = User.objects.all().filter(groups__name="Delivery Crew").get(pk=pk)
        delivery_crew = Group.objects.get(name="Delivery Crew")
        delivery_crew.user_set.remove(user)
        return Response(
            {"message": "user removed from the delivery crew group"},
            status=status.HTTP_200_OK,
        )