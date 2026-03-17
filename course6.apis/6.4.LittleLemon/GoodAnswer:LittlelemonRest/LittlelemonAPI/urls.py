from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<str:title>', views.SingleMenuItemView.as_view(), name='SingleMenuItem' ),
    path('groups/<str:group_name>/users', views.ManagersViewSet.as_view()),
    path('groups/<str:group_name>/users/<int:pk>', views.ManagerViewSetSingleUser.as_view()),
    path('cart/menu-items', views.CartView.as_view()),
    path('orders', views.OrderView.as_view()),
    path('orders/<int:pk>', views.OrderItemView.as_view())
]
