# Generated by Django 5.1.1 on 2024-10-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_like_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='likecount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
