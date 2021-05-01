from django.urls import path,include 
from .views import item_categories, ItemDetail


app_name = 'product'

urlpatterns = [ 

path('',item_categories, name = 'item-list'),
path('detail/<int:pk>/', ItemDetail.as_view(), name = 'detail'),
 
]