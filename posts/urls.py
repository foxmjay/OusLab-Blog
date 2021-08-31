from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('/create', views.post_create, name='post_create'),
    path('/store', views.post_store, name='post_store'),
    path('/delete/<int:post_id>', views.post_delete, name='post_delete'),
    path('/edit/<int:post_id>', views.post_edit, name='post_edit'),
    path('/update/<int:post_id>', views.post_update, name='post_update'),
    path('/show/<str:post_url>', views.post_details, name='post_details'),
    path('/options/<int:post_id>', views.post_options, name='post_options'),
    path('/storetag/<int:post_id>', views.store_tag, name='store_tag'),
    path('/removetag/<int:post_id>', views.remove_tag, name='remove_tag'),
    path('/storecategorie/<int:post_id>', views.store_categorie, name='store_categorie'),
    path('/removecategorie/<int:post_id>', views.remove_categorie, name='remove_categorie'),
]
