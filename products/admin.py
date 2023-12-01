from django.contrib import admin
from products.models import Product, ProductCategory

admin.site.register(ProductCategory)
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    search_fields = ('name', 'price', 'quantity', 'category')
    ordering = ('-name',)