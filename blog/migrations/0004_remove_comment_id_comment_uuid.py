# Generated by Django 5.1.2 on 2024-11-11 10:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_comments_comment_post_alter_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.AddField(
            model_name='comment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]