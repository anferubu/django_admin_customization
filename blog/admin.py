from django.contrib import admin

from . import models


class MyAdminSite(admin.AdminSite):
    site_header = 'Blog administration panel'
    site_header = 'Blog Admin'
    index_title = 'Blog site administration'
    app_index_template = 'blog/admin/blog/app_index.html'


admin_site = MyAdminSite(name='my_admin')

@admin.register(models.Comment, site=admin_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'body', 'created', 'active']
    exclude = ['email']
    list_filter = ['user', 'post', 'created', 'active']
    search_fields = ['user', 'post', 'body']
    date_hierarchy = 'created'
    ordering = ['active', 'created']


admin_site.register(models.Contact)
admin_site.register(models.Post)
admin_site.register(models.Tag)