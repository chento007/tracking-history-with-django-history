# Generated by Django 4.2.6 on 2023-10-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0018_remove_historicalhistory_dynamic_field_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalhistory',
            name='changed',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='changed',
            field=models.CharField(max_length=255, null=True),
        ),
    ]