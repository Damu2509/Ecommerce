from django.urls import path, include
from .views import home, ItemCategories

app_name = 'products'

urlpatterns = [
    
    path('', home, name= 'home'),
    path('itemcategories/', ItemCategories.as_view(), name= 'itemcategories')

]