from django.db import models
from django.utils import timezone


class ViewLog(models.Model):
    ip = models.CharField(max_length=250, blank=True, default='')
    agent = models.CharField(max_length=250, blank=True, default='')
    host = models.CharField(max_length=250, blank=True, default='')
    url = models.CharField(max_length=250, blank=True, default='')
    referer = models.CharField(max_length=250, blank=True, default='')
    country = models.CharField(max_length=250, blank=True, default='')
    created_at = models.DateTimeField(auto_now=True)
