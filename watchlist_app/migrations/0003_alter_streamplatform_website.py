# Generated by Django 4.2.6 on 2023-10-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_streamplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='website',
            field=models.URLField(max_length=100),
        ),
    ]
