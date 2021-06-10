from django.shortcuts import render

from django.http import HttpResponse



def demo(request):

    return HttpResponse("<h1>  This is under the mess that is deleted </h1>")


