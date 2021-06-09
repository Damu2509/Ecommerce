from django.db import models

# Create your models here.

class Items(models.Model):

    category  = models.CharField( max_length = 100)
    title = models.CharField( max_length = 250 )
    image_url  = models.CharField(max_length = 250, null= True)
    tag = models.CharField( max_length = 100 )
    description = models.TextField()
    price  = models.IntegerField( default = 0 )
