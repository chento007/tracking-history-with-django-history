# Generated by Django 4.2.6 on 2023-10-23 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0008_rename_updated_review_update_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='active',
        ),
        migrations.RemoveField(
            model_name='review',
            name='created',
        ),
        migrations.RemoveField(
            model_name='review',
            name='description',
        ),
        migrations.RemoveField(
            model_name='review',
            name='update',
        ),
        migrations.RemoveField(
            model_name='review',
            name='watchlist',
        ),
    ]
