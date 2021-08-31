from django.urls import path

from . import views

urlpatterns = [
    path('', views.categorie_list, name='categorie_list'),
    path('/create', views.categorie_create, name='categorie_create'),
    path('/store', views.categorie_store, name='tag_store'),
    path('/delete/<int:categorie_id>', views.categorie_delete, name='categorie_delete'),
    path('/edit/<int:categorie_id>', views.categorie_edit, name='categorie_edit'),
    path('/update/<int:categorie_id>', views.categorie_update, name='categorie_update'),
]
