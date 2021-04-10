from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from product.models import Products

from .models import Products
from django.forms import forms


def product_detail_view(request):
    return render(request, 'product/product_detail.html', {'name':'ecommerce'})


class ProductForm():
    model = Products
    obj = Products.objects.all()
    fields = ['title','description','type']
    return render(request, 'product/form.html', {'obj':obj})