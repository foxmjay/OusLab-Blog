from django.db import models
from posts.models import Post


class Comment(models.Model):
    stringid = models.CharField(max_length=250, blank=False)
    username = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=250, blank=False)
    message = models.TextField(blank=True, default='')
    data = models.CharField(max_length=250, blank=True, default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
