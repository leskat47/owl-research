from django.contrib import admin
from .models import Client, Project, Content, Metric, Note, User


class ProjectInline(admin.TabularInline):
    model = Project


class NoteInline(admin.StackedInline):
    model = Note


class ContentInline(admin.StackedInline):
    model = Content

    fields = (('name',
               'user',
              'outlet',
              'author',
              ),
              (
                'url',
                'date',
                'metric'
               ))


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
