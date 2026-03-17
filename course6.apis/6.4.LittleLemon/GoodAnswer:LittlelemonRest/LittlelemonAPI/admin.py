from django.contrib import admin
from .models import Category, MenuItem, User, Cart, Order
# Register your models here.

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Order)