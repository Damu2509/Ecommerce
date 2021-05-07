from django.contrib import admin


from .models import ItemCategories,ItemDetail,ToDoList,Item

admin.site.register(ItemCategories)
admin.site.register(ItemDetail)
admin.site.register(ToDoList)
admin.site.register(Item)

