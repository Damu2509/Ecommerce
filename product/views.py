from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import ItemCategories, ItemDetail, ToDoList, Item

from .forms import CreateNewList

class CategoryList(ListView):

    model = ItemCategories
    template_name = 'product/item_categories.html'
    paginate_by =1

class ItemDetail(DetailView):
    model = ItemDetail
    template_name = 'product/item_detail.html'

class Item(DetailView):
    model = Item
    template_name = 'product/item_detail.html'

def itemCreate(response):

    if response.method == "POST":

        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, 'product/items.html', {'form':form})
    
    
