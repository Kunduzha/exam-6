from django.contrib import admin
from webapp.models import Comments


# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    comment_display = ['id', 'name', 'email', 'comment', 'status']
    list_filter = ['name', 'email']
    search_fields = ['name', 'comment']
    fields = ['id', 'name', 'email', 'comment', 'status', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Comments, CommentAdmin)
