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

class ToDoList(models.Model):

  name = models.CharField(max_length = 100)

  def __str__(self):

    return se;f.name

class Item(models.Model):

  todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
  text = models.CharField(max_length = 300)
  complete = models.BooleanField()
  
  def __str__(self):

    return self.text

  


  





   

