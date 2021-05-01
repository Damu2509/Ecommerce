from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse

from .models import ItemCategories



def item_categories(request):

    context = {
        'items' : ItemCategories.objects.all()
    }

    return render(request, 'product/item_categories.html', context)
