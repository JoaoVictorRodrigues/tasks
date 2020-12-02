from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.get_all_tasks, name='get'),
    path('post/', views.get_all_tasks, name='post'),
]
