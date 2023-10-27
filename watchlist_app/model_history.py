from simple_history.models import HistoricalRecords
from django.db import models
from django.contrib.auth.models import User


class History(models.Model):
    name = models.CharField(max_length=255,null=True)
    history_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    changed = models.CharField(max_length=255,null=True)
    history= HistoricalRecords()

