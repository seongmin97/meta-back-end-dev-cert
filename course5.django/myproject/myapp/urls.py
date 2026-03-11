from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="home"), 
    # path('menu/', views.menu, name="menu"),
    # path('aboutus/', views.about, name="about"),
    # path('book/', views.book, name="book"),
    path('drinks/<str:drink_name>', views.drinks, name="drinks"),
    path('booking/', views.form_view, name="booking"),
    # path('menu/', views.menu),
    # path('about/', views.about),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
    
] 