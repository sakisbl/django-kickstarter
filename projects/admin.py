from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal', 'amountRaised', 'creator', 'created']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)
