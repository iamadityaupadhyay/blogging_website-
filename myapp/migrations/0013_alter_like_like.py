# Generated by Django 5.1.1 on 2024-10-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_like_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
