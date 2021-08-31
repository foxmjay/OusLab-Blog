from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewlog_list, name='viewlog_list'),
    path('/delete/<int:viewlog_id>', views.viewlog_delete, name='viewlog_delete'),
]