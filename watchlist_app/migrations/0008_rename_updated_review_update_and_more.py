# Generated by Django 4.2.6 on 2023-10-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_alter_review_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='updated',
            new_name='update',
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
