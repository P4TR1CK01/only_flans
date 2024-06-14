from django.urls import path
from main.views import index, about, welcome, contact, success, ayuda, register

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('contact/', contact),
    path('success/', success),
    path('help/', ayuda),
    path('register/', register),
]

