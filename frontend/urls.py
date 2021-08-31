from django.urls import path

from . import views
from comments.views import comment_store

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<str:post_url>', views.post_details, name='post_details'),
    path('tech_snippets', views.tech_snippets, name='tech_snippets'),
    path('posts/tag/<int:tag_id>', views.postByTag, name='postByTag'),
    path('posts/categorie/<int:categorie_id>', views.postByCategorie, name='postByCategorie'),
    path('comments/send/<int:post_id>', comment_store, name='comment_store'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('search', views.post_search, name='post_search'),
]
