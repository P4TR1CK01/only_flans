from django.urls import path
from main.views import index, about, welcome, success

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('success/', success),
]

