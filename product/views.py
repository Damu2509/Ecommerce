from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import ItemCategories, ItemDetail

from .forms import CreateNewList

class CategoryList(ListView):

    model = ItemCategories
    template_name = 'product/item_categories.html'
    paginate_by =1

class ItemDetail(DetailView):
    model = ItemDetail
    template_name = 'product/item_detail.html'

def itemCreate(request):
    form = CreateNewList()
    return render(request, 'product/items.html', {'form':form})
    
    
