# Generated by Django 5.1.1 on 2024-10-11 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_like_likecount'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]