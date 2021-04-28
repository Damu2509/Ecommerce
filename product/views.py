from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse

from .models import Item



def item_list(request):

    context = {
        'items' : Item.objects.all()
    }

    return render(request, 'product/home-page.html', context)
