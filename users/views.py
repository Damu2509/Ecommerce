from django.shortcuts import render
from product.forms import RegisterForm
# Create your views here.



def register(request):

        form = RegisterForm(request.POST or None)

        if form.is_valid():
            form.save()
            form = RegisterForm(request.POST or None)

        context = {
            'form':form
        }

        return render(request, 'users/register.html', context)