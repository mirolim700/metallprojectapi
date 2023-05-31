from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UsersView.as_view()),
    path('user/<int:pk>/', UsersView.as_view()),
    path('product/', ProductsView.as_view()),
    path('productById/<int:pk>/', ProductByIdView.as_view()),
    path('info/', InfoView.as_view()),
]