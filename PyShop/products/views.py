from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

#mainpage
#parameter is the http request


def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{"products": products})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'details.html', {'product': product})

def new(request):
    return HttpResponse("new product")