# Generated by Django 4.2.6 on 2023-10-24 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0012_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='watchlist_app.user'),
            preserve_default=False,
        ),
    ]
