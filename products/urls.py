from django.urls import path, include
from .views import home, itemCategories

app_name = 'products'

urlpatterns = [
    
    path('', home, name= 'home'),
    path('itemcategories/', itemCategories.as_view(), name= 'itemcategories')

]