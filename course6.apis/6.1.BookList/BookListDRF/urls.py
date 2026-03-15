from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view(), name = 'SingleBook'),
]