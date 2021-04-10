from django.urls import path,include 
from .views import product_detail_view, ProductForm

urlpatterns = [ 
    path('detail/', product_detail_view, name = 'detail'),
    path('form/', ProductForm, name = 'form')

]