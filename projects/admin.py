from django.contrib import admin
from .models import Project
from unfold.admin import ModelAdmin


class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
admin.site.register(Project)