from django.shortcuts import render

from django.http import HttpResponse



def home(request):

    return render(request, 'products/base.html', {'name' : 'This is the site '})


def demo(request):

    return HttpResponse("<h1>  This is under the mess that is deleted </h1>")


