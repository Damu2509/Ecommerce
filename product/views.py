from django.shortcuts import render,get_object_or_404,redirect

from django.http import HttpResponse

from product.models import Products

from .models import Products
from django.forms import forms

from .forms import ProductForm, RawProductForm


def raw_create_view(request):

    my_form = RawProductForm()

    if request.method == "POST":

      my_form = RawProductForm(request.POST or None)

      if my_form.is_valid():
        
          Products.objects.create(**my_form.cleaned_data)
          my_form = RawProductForm()

    context = {
      'form' : my_form,
    }

    return render(request, 'product/product_create.html', context)


def product_create_view(request):

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form': form
    }

    return render(request, 'product/product_create.html', context)

def product_detail_view(request,id):
    
    obj = Products.objects.get(id = id)
    context = {
        'object' : obj 
    }
    return render(request, 'product/product_detail.html', context)

def product_delete_view(request,id):
    
    obj = Products.objects.get(id = id)

    form = ProductForm(request.POST)
    context = {
        'object' : obj 
    }

    if request.method == 'POST':
       obj.delete()
       return redirect('../../')
    
    return render(request, 'product/product_delete.html', context)


def product_list_view(request):
    lists = Products.objects.all()

    form = ProductForm(request.POST)

    context = {
        'object' : lists
    }

    return render(request, 'product/product_list.html', context)


from django.views.generic import (ListView,DetailView)
from .models import Products

class ProductListView(ListView):
    queryset = Products.objects.all()
    template_name = 'product/product_list.html'

    context = {
        'objects' : queryset
    }

    def get_object(self,request):
        id_ = self.kwargs.get("id")
        #return get_object_or_404(Products, id = id_)

        context = {
        'objects' : Products.objects.all()
    }
        return render(request, 'product/product_list.html', context)

class ProductDetailView(DetailView):
    queryset = Products.objects.all()

    template_name = 'product/product_detail.html'

    context = {
        'objects' : queryset
    }


    def get_object(self):
        id_ = self.kwargs.get("id")
        #return get_object_or_404(Products, id = id_)
        return request(request, 'product/product_list.html', context)

