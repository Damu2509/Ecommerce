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




from django.views.generic import (ListView,DetailView,UpdateView,CreateView,DeleteView)
from .models import Products
from .forms import ProductForm
from django.urls import reverse

class ProductListView(ListView):
    queryset = Products.objects.all()
    template_name = 'product/product_list.html'

  
class ProductDetailView(DetailView):
    
    queryset = Products.objects.all()

    a = Products.objects.all() 

    template_name = 'product/product_detail.html'

    def get_object(self):

        id1 = self.kwargs.get("id") 

        return get_object_or_404(Products, id =id1 )



class ProductCreateView(CreateView):
    
    queryset = Products.objects.all()

    form_class = ProductForm

    template_name = 'product/product_create.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().from_valid(form)



class ProductDeleteView(DeleteView):
    
    queryset = Products.objects.all()

    template_name = 'product/product_delete.html'

    def get_object(self):

        id1 = self.kwargs.get("id") 

        return get_object_or_404(Products, id =id1 )

    def get_success_url(self):
        return reverse("product:ProductListViews")



from django.views import View

class functiondetailview(View):
    template_name = 'product/product_list.html'

    def get(self, request, id=None, *args, **kwargs):

        context = {}

        if id is not None:
            obj = get_object_or_404(Products, id = id)
            context['object'] = obj

        return render(request, self.template_name, context)

class ProductRawList(View):

    template_name = 'product/product_list.html'
    queryset = Products.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'object_list' : self.queryset})

class Inherited(ProductRawList):
    queryset = Products.objects.filter(id = 1)
    
