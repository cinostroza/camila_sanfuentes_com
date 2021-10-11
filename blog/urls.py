from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='blog_index'),
    path('post_detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new_post/', views.NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post_publish/<int:pk>', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/post_list', views.PostList.as_view(), name='post_list')
]
