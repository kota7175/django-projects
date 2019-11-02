from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('<int:blog_id>/publishing/', views.publishing, name='publishing'),
    path('<int:blog_id>/unpublishing/', views.unpublishing, name='unpublishing'),
    path('<int:blog_id>/detail/', views.detail, name='detail'),
    path('<int:blog_id>/edit/', views.edit, name='edit'),
    path('<int:blog_id>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:blog_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:blog_id>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:blog_id>/remove/', views.comment_remove, name='comment_remove'),
]