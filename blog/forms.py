from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post

class PostForm(forms.ModelForm):
    """
    Form to create a blog post
    """
    class Meta:
        model = Post
        fields = ['title', 'image', 'image_alt', 'excerpt', 'content', 'status']

        content = forms.CharField(widget=SummernoteWidget())

        widget = {
            "excerpt": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            'title': 'Title',
            'image': 'Image',
            'image_alt': 'Describe Image',
            'excerpt': 'Description',
            'content': 'Content',
            'status': 'Status',
        }