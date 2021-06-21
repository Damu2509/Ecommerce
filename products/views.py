from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Items, itemCategories


class itemCategories(ListView):

    model = itemCategories
    template_name = 'products/itemCategories.html'

class items(ListView):

    model = Items
    template_name = 'products/items.html'

def itemsAll(request):

    itemsAll = Items.objects.all()

    context = { 'items': itemsAll }

    return render(request, 'products/items.html', context)


    

