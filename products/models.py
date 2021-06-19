from django.db import models

# Create your models here.

class itemCategories(models.Model):

    category  = models.CharField( max_length = 100, null = True)
    title = models.CharField( max_length = 250, null = True )
    image_url  = models.CharField(max_length = 250, null= True)
  
class Items(models.Model):

    title = models.CharField(max_length  = 250, null = True)
    image_url = models.CharField(max_length =  250 , null = True)
    tag = models.CharField( max_length = 100, null = True )
    description = models.TextField()
    price  = models.IntegerField( default = 0, null = True )


