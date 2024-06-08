from django.urls import path
from main.views import index, about, welcome, success, ayuda

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('success/', success),
    path('help/', ayuda),

]

