# Generated by Django 4.2.6 on 2023-10-27 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0014_history_historicalhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalhistory',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
