# Generated by Django 5.0.1 on 2024-01-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlShort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortlink',
            name='short_url_key',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
