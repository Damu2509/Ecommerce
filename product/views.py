from django.shortcuts import render

from django.http import HttpResponse

from product.models import Products

def product_detail_view(request):
    return HttpResponse("<h1> This is with respect to the ecommerce site</h1>")