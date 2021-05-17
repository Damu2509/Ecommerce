from django.urls import path,include 
from .views import ItemDetail, CategoryList, itemCreate, Item


app_name = 'product'

urlpatterns = [ 

path('',CategoryList.as_view(), name = 'item-list'),
path('<int:pk>/', ItemDetail.as_view(), name = 'detail'),
path('items/', itemCreate, name = 'item-create'),
 
]