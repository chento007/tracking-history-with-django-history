# Generated by Django 4.2.6 on 2023-10-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0009_remove_review_active_remove_review_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
