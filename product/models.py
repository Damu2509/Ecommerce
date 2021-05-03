from django.db import models
from django.conf import settings

  # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class ItemCategories( models.Model ):
     
    category = models.CharField(max_length = 25)
    image = models.ImageField(upload_to = 'media/', null = True, blank = True)


class ItemDetail(models.Model):

  title = models.CharField(max_length = 50)
  description = models.TextField(max_length = 1000)
  tag = models.CharField(max_length = 50)
  price = models.FloatField(default=00.00)
  discount = models.FloatField()
  image = models.ImageField(blank = True, null = True) 


  


  





   

