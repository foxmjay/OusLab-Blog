from django.db import models

from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from posts.models import Post
import random
import os
import string


def user_directory_path(instance, filename):
    random_prefix = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
    return 'uploads/{0}_{1}'.format(random_prefix, filename)


class Library(models.Model):
    path = models.FileField(upload_to=user_directory_path)
    ltype = models.CharField(max_length=100, default='image')

    def delete(self, using=None, keep_parents=False):

        file_path = self.path.storage
        print(self.path.name)
        if file_path.exists(self.path.name):
            self.path.delete(save=False)
        super().delete()
