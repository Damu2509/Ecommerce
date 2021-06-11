from django.urls import path, include
from .views import home,demo

app_name = 'products'

urlpatterns = [
    
    path('', home, name= 'home'),
    path('demo/', demo, name= 'demo')

]