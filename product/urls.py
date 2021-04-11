from django.urls import path,include 
from .views import product_detail_view, product_create_view

urlpatterns = [ 
    path('detail/', product_detail_view, name = 'detail'),
    path('create/', product_create_view, name = 'create'),

]