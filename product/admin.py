from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'price',
                    'updated_at', 'created_at',)
    ordering = ('-id',)
    search_fields = ('name',)