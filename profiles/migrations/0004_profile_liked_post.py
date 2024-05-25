# Generated by Django 5.0.6 on 2024-05-22 19:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_alter_profile_bio"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="liked_post",
            field=models.ManyToManyField(
                blank=True, related_name="liked_post", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]