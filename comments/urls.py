from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('/create/<int:post_id>', views.comment_store, name='comment_store'),
    path('/delete/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
