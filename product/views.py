from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse
from django.views.generic import DetailView

from .models import ItemCategories, ItemDetail



def item_categories(request):

    context = {
        'items' : ItemCategories.objects.all()
    }

    return render(request, 'product/item_categories.html', context)

class ItemDetail(DetailView):
    model = ItemDetail
    template_name = 'product/product_detail.html'
    
    
