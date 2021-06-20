from django.urls import path, include
from .views import home, itemCategories, items, itemsAll

app_name = 'products'

urlpatterns = [
    
    path('', home, name= 'home'),
    path('itemcategories/', itemCategories.as_view(), name= 'itemcategories'),
    path('itemlist/', items.as_view(), name = 'itemlist'),
    path('itemsall/', itemsAll, name= 'items-all'),


]