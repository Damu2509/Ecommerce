from django.shortcuts import render
from product.forms import RegisterForm
# Create your views here.

from django.contrib.auth.forms import UserCreationForm

def register(request):

        form = UserCreationForm()

        if form.is_valid():
            form.save()
            form = RegisterForm(request.POST or None)

        context = {
            'form':form
        }

        return render(request, 'users/register.html', context)