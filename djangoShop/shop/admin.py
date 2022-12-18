from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    field = ('name', 'stock', 'price', 'image')

admin.site.register(Product)
