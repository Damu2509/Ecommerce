from django.urls import path,include 
from .views import ItemDetail, CategoryList, itemCreate, Item, itemCategories, trial , register


app_name = 'product'

urlpatterns = [ 

path('',CategoryList.as_view(), name = 'item-list'),
path('<int:pk>/', ItemDetail.as_view(), name = 'detail'),
path('items/', itemCreate, name = 'item-create'),
path('itemcategories/', itemCategories, name = 'item-category'),
path('trial/', trial, name = 'trial'),
path('register/', register, name = 'register'),


 
]