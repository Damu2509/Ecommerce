from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from product.models import Products

from .models import Products
from django.forms import forms


def product_detail_view(request):
    
    obj = Products.objects.get(id = 1)
    context = {
        'object' : obj 
    }
    return render(request, 'product/product_detail.html', context)