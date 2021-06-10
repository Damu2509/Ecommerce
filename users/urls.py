from django.urls import path, include

from .views import userRegistration

app_name = 'users'

urlpatterns = [

path('register/', userRegistration, name = 'registration')

]