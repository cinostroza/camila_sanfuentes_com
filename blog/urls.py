from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='blog_index'),
    path('post_detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('new_post/', views.NewPost.as_view(), name='new_post'),
    path('post_publish/<int:pk>', views.post_publish, name='post_publish'),
    path('post_list', views.PostList.as_view(), name='post_list')
]
