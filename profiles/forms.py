from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    A form so User can create a profile
    """

    class Meta:
        model = Profile
        fields = ["image", "bio"]

        labels = {"image": "Avatar", "bio": "Bio"}
