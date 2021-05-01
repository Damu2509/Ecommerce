from django.urls import path,include 
from .views import item_categories


app_name = 'product'

urlpatterns = [ 

path('',item_categories, name = 'item-list'),
 
]