from django.contrib import admin
from .models import ProjectModel, IssueModel, CommentModel
# Register your models here.
@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'owner', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title', 'owner__username']
    list_filter = ['owner']
    list_per_page = 15
    ordering = ['-id']
    autocomplete_fields = ['owner']


@admin.register(IssueModel)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'project', 'reporter', 'assignee', 'status', 'priority', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']
    list_filter = ['project', 'reporter', 'assignee', 'status', 'priority', 'created_at']
    list_per_page = 15
    ordering = ['-id']
    autocomplete_fields = ['project', 'reporter', 'assignee']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'issue', 'user']
    autocomplete_fields = ['issue', 'user']