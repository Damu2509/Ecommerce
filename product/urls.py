from django.urls import path,include 
from .views import product_detail_view, product_create_view, raw_create_view, product_delete_view

urlpatterns = [ 
    path('detail/<int:id>/', product_detail_view, name = 'detail'),
    path('create/', product_create_view, name = 'create'),
    path('raw-form/', raw_create_view, name = 'raw-form'),

    path('delete/<int:id>/', product_delete_view, name = 'delete-view'),


]