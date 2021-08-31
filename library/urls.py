from django.urls import path
from . import views

urlpatterns = [
    path('/store', views.image_store, name='image_store'),
    path('/delete', views.image_delete, name='image_delete'),
]