from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import random
import os
from django.urls import reverse


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        filename = str(random.randint(10, 99)) + str(random.randint(10, 99)) + str(random.randint(10, 99)) + str(random.randint(10, 99)) + "_" + filename
        return os.path.join(self.path, filename)


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="user", null=True)
    title = models.CharField(max_length=250, blank=True, default='')
    front_image = models.ImageField(upload_to=PathAndRename("uploads"), blank=True, null=True)
    content_image = models.ImageField(upload_to=PathAndRename("uploads"), blank=True, null=True)
    url_title = models.CharField(max_length=250, blank=True, default='')
    published = models.BooleanField(default=False)
    description = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')
    post_type = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    published_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)
    fb_comment_url = models.TextField(blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Post, self).save(*args, **kwargs)

    def delete_front_image(self):
        front_image = self.front_image.storage
        if front_image.exists(self.front_image.name):
            self.front_image.delete(save=False)

    def delete_content_image(self):
        content_image = self.content_image.storage
        if content_image.exists(self.content_image.name):
            self.content_image.delete(save=False)

    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.url_title)])
