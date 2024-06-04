from django.urls import path
from main.views import index, about, welcome

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome)

]
