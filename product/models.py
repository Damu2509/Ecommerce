from django.db import models
from django.conf import settings

  # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class ItemCategories( models.Model ):
    
    category = models.CharField(max_length = 25)
    image = models.ImageField(null = True, blank = True)





   

