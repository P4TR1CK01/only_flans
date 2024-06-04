from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indice(req):
  return render(req, 'index.html')