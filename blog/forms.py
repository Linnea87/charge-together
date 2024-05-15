from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form to create a blog post
    """

    class Meta:
        model = Post
        fields = [
            "title",
            "image",
            "image_alt",
            "excerpt",
            "content",
            "status",
        ]

        widgets = {
            "excerpt": forms.Textarea(attrs={"rows": 5}),
            "content": SummernoteWidget(),
        }

        labels = {
            "title": "Title",
            "image": "Image",
            "image_alt": "Describe Image",
            "excerpt": "Excerpt",
            "content": "Content",
            "status": "Status",
        }
