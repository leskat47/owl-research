from django.contrib import admin
from .models import Client, Project, Content, Metric, Note, Staff


class ProjectInline(admin.TabularInline):
    model = Project


class NoteInline(admin.TabularInline):
    model = Note
    list_display = ('name', 'url', 'outlet', 'author', 'date', 'staff')
    list_display_links = ('name',)

class ContentInline(admin.TabularInline):
    model = Content


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ContentInline]



@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    inlines = [NoteInline]


admin.site.register(Metric)
admin.site.register(Staff)
