from django.http import HttpResponse
from django.shortcuts import render
from .models import Product



def index(request):
    products = Product.objects.all()
    print("products")
    print(products)
    return render(request,"index.html",{"products":products})

def new(request):
    return HttpResponse("Hello, New.")