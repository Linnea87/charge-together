from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Register info from contact form in admin panel
    """

    list_display = (
        "name",
        "email",
        "read",
    )
