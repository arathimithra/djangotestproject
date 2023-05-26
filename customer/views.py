from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return HttpResponse("hai..")

def message(request):
    return HttpResponse("welcome")

def myhtml(request):
    return render(request,'my.html')