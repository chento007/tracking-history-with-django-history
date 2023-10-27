from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.


class StreamPlatform(models.Model):

    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):

    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=255)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=30)


class Review(models.Model):

    review_user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(
        WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)