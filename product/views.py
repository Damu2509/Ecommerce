from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import ItemCategories, ItemDetail

class CategoryList(ListView):

    model = ItemCategories
    template_name = 'product/item_categories.html'

class ItemDetail(DetailView):
    model = ItemDetail
    template_name = 'product/item_detail.html'
    
    
