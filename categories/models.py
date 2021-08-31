from django.db import models

from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from posts.models import Post
import random
import os


class Categorie(models.Model):

    name = models.CharField(max_length=250)
    posts = models.ManyToManyField(Post)
