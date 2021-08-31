from django.db import models

from django.contrib.sitemaps import Sitemap
from posts.models import Post
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.6

    def items(self):
        return Post.objects.filter(deleted=False, published=True)

    def lastmod(self, obj):
        return obj.published_at

    def location(self, item):
        return '/posts/%s' % (item.url_title)
