from django.shortcuts import render
from .forms import UserRegistration

def userRegistration(request):

    form = UserRegistration(request.POST)

    return render(request, 'users/userRegistration.html', {'form' : form})
