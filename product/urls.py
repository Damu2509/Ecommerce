from django.urls import path,include 
from .views import product_detail_view

urlpatterns = [ 
    path('detail/', product_detail_view, name = 'detail'),
    

]