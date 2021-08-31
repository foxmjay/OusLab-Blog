"""OusLabBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
import backend,posts
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap 
from django.views.generic.base import TemplateView

from frontend.models import BlogSitemap

from posts.models import Post

sitemaps = {
    'static': BlogSitemap,
}


info_dict = {
    'queryset': Post.objects.filter(deleted=False,published=True),
}

urlpatterns = [
    path('', include('frontend.urls')),
    re_path(r'^dashboard/', include('backend.urls')),
    re_path(r'^dashboard/posts', include('posts.urls')),
    re_path(r'^dashboard/tags', include('tags.urls')),
    re_path(r'^dashboard/categories', include('categories.urls')),
    re_path(r'^dashboard/comments', include('comments.urls')),
    re_path(r'^dashboard/library', include('library.urls')),
    re_path(r'^dashboard/viewlogs', include('views_log.urls')),


    path('login', backend.views.dashboard_login, name='dashboard_login'),
    path('logout', backend.views.dashboard_logout, name='dashboard_logout'),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    
    #path('sitemap.xml', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}}, name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), ),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)