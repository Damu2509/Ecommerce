from django.urls import path,include 
from .views import item_list


app_name = 'product'

urlpatterns = [ 

path('',item_list, name = 'item-list'),
 
]