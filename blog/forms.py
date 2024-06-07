from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Post, Comment


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

        content = forms.CharField(widget=RichTextWidget())

        widgets = {
            "excerpt": forms.TextInput(attrs={"class": "form-control"}),
        }

        labels = {
            "title": "Title",
            "image": "Image",
            "image_alt": "Describe Image",
            "excerpt": "Excerpt",
            "content": "Content",
            "status": "Status",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
