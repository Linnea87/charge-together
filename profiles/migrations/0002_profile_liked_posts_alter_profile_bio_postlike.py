# Generated by Django 5.0.6 on 2024-05-29 19:47

import django.db.models.deletion
import djrichtextfield.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_comment_delete_posts"),
        ("profiles", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="liked_posts",
            field=models.ManyToManyField(
                blank=True, related_name="liked_posts", to="blog.post"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=djrichtextfield.models.RichTextField(
                blank=True, max_length=2500, null=True
            ),
        ),
        migrations.CreateModel(
            name="PostLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
