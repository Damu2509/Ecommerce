from django.urls import path,include 
from .views import ItemDetail, CategoryList


app_name = 'product'

urlpatterns = [ 

path('',CategoryList.as_view(), name = 'item-list'),
path('detail/<int:pk>/', ItemDetail.as_view(), name = 'detail'),
 
]