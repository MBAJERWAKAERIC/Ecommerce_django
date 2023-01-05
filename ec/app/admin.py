from django.contrib import admin
from . models import Product

# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discouted_price', 'category' 'product_image']
