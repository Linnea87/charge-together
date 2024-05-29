from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
        "created_on",
        "image",
    )
    search_fields = ["title", "content"]
    list_filter = (
        "status",
        "created_on",
    )
    summernote_fields = ("content")

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'image', 'excerpt', 'content', 'status', 'likes'),
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'body', 'post', 'created_on')