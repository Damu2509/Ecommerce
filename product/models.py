from django.db import models

from django.urls import reverse

class Products(models.Model):

    title       = models.TextField(max_length = 100)
    type        = models.CharField(max_length = 50)
    description = models.TextField(max_length = 200)
    price       = models.DecimalField(decimal_places = 2,max_digits = 7,default = 0.00)

    def get_absolute_url1(self):
        return f"/product/detail/{self.id}/"

   

