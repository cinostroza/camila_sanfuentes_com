from django.urls import path
from gallery import views

app_name = 'gallery'

urlpatterns = [
    path('', views.GalleryIndex.as_view(), name='index'),
    path('<str:gallery_name>', views.GalleryView.as_view(), name='gallery'),
]
