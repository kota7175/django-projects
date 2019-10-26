from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:blog_id>/publishing/', views.publishing, name='publishing'),
    path('<int:blog_id>/unpublishing/', views.unpublishing, name='unpublishing'),
]