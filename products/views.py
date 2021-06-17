from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Items

def home(request):

    return render(request, 'products/base.html', {'name' : 'This is the site '})

class ItemCategories(ListView):

    model = Items
    template_name = 'products/itemCategories.html'


