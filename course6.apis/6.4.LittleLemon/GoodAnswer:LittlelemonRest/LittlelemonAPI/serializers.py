from .models import MenuItem, Category, Cart, Order, OrderItem, User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.utils.text import slugify

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']
        extra_kwargs = {'slug': {'required': False}}

    def create(self, validated_data):
        # If the user didn't provide a slug, create one from the title
        if 'slug' not in validated_data:
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)

class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category', read_only=True) 
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    title = serializers.CharField(max_length=255, validators=[UniqueValidator(queryset=MenuItem.objects.all())])
    featured = serializers.BooleanField()

    class Meta:
        model = MenuItem 
        fields = ['id','title','price','category_name','category','featured']
        # extra_kwargs = {
        #     'category': {'write_only': True}, # This hides category ID in GET, but allows it in POST
        # }


class CartSerializer(serializers.ModelSerializer):
    menuitem = serializers.SlugRelatedField(
        queryset = MenuItem.objects.all(),
        slug_field = 'title'
    )
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    
    class Meta:
        model = Cart 
        fields = ['id', 'menuitem', 'quantity', 'unit_price', 'price']


class OrderItemSerializer(serializers.ModelSerializer):

    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    menuitemname = serializers.StringRelatedField(source='menuitem', read_only=True) # show the name of the item during GET request

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menuitem','menuitemname', 'quantity', 'unit_price', 'price']


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')
    total = serializers.DecimalField(read_only=True, max_digits=6, decimal_places=2)
    date = serializers.DateField(read_only=True)
    delivery_crew = serializers.SlugRelatedField(
        queryset = User.objects.filter(groups__name='Delivery crew'),# allows only users that are in delivery crew group to be selected
        slug_field = 'username', # allows the username to be sent in request and received in response instead of id
        allow_null = True,
        required = False
    ) 

    class Meta:
        model = Order
        fields = ['id', 'delivery_crew', 'status', 'total', 'date', 'items']