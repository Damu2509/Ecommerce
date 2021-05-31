from django.urls import path, include
from .views  import register

app_name = 'users'

urlpatterns = [

    path('register/', register, name = 'register'),

]