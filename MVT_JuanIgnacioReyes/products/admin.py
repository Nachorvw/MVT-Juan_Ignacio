from django.contrib import admin

# Register your models here.
from products.models import Products

#admin.site.register(Products)
#? para agregar el products en la parte de admin del django
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "available",) #? que te muestre el nombre precio y stock
    list_filter = ("price", "available",)#? para agregar el poder filtrar (este caso por precio y stock)
    search_fields = ("name",) #? para agregar el buscador por (este caso nombre)