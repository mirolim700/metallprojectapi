from django.urls import path
from .views import *

urlpatterns = [
    path('user/',UserView.as_view()),
    path('product/',ProductView.as_view()),
    path('product/<int:pk>/',ProductByIdView.as_view()),
    path('info/',InfoView.as_view())
]