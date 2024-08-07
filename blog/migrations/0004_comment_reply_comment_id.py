# Generated by Django 5.0.7 on 2024-07-30 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_managers_alter_comment_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply_comment_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment'),
        ),
    ]
