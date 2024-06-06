from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'body', 'post', 'created_on')