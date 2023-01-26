from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from . import models




@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'body', 'created', 'active']
    exclude = ['email']
    list_filter = ['user', 'post', 'created', 'active']
    search_fields = ['user', 'post', 'body']
    date_hierarchy = 'created'
    ordering = ['active', 'created']


admin.site.register(models.Contact)
admin.site.register(models.Post)
admin.site.register(models.Tag)