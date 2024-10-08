# Generated by Django 4.2 on 2024-02-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlShort', '0004_shortlink_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortlink',
            name='slug',
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='short_code',
            field=models.SlugField(max_length=4, unique=True),
        ),
    ]
