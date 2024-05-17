from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile


class ProfileAdmin(SummernoteModelAdmin):
    list_display = (
        "pk",
        "user",
        "bio",
        "image"
    )
admin.site.register(Profile, ProfileAdmin)