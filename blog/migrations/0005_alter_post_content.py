# Generated by Django 5.0.6 on 2024-06-06 17:07

import djrichtextfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
