from django.urls import path
from . import views

urlpatterns = [
    path('', views.tag_list, name='tag_list'),
    path('/create', views.tag_create, name='tag_create'),
    path('/store', views.tag_store, name='tag_store'),
    path('/delete/<int:tag_id>', views.tag_delete, name='tag_delete'),
    path('/edit/<int:tag_id>', views.tag_edit, name='tag_edit'),
    path('/update/<int:tag_id>', views.tag_update, name='tag_update'),
]
