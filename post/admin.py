from django.contrib import admin
from .models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'updated_at', 'created_at',)
    ordering = ('-id',)
    search_fields = ('user',)