from django.urls import path, include
from .views import demo

app_name = 'products'

urlpatterns = [
    path('demo/', demo, name= 'demo')
]