from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for contacting the resort.
    """
    class Meta:
        """
        Specifies the django model and order of the fields
        """
        model = Contact
        fields = (
            'name',
            'email',
            'message',
        )