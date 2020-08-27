from django.contrib import admin
from . models import Blog




class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'time']
    ordering = ['text']




admin.site.register(Blog, BlogAdmin)
