from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from product.models import Products

from .models import Products
from django.forms import forms

from .forms import ProductForm


def product_create_view(request):

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form': form
    }

    return render(request, 'product/product_create.html', context)

def product_detail_view(request):
    
    obj = Products.objects.get(id = 1)
    context = {
        'object' : obj 
    }
    return render(request, 'product/product_detail.html', context)