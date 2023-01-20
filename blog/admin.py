from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'content', 'created','link']


admin.site.register(Post, PostAdmin)

