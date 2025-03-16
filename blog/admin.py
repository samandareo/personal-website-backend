from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import BlogPost

class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'views')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at', 'author')



admin.site.register(BlogPost, BlogPostAdmin)
