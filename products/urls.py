from django.urls import path, include
from .views import home, itemCategories, items,boot, boot1

app_name = 'products'

urlpatterns = [
    
    path('', home, name= 'home'),
    path('itemcategories/', itemCategories.as_view(), name= 'itemcategories'),
    path('itemlist/', items.as_view(), name = 'itemlist'),
    path('boot/', boot),
    path('boot1/', boot1)


]