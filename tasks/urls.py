from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.get_all_tasks, name='get'),
    path('post/', views.post_task, name='post'),
    path('delete/', views.delete_tasks, name='delete'),
]
