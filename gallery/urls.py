from django.urls import path
from gallery import views

app_name = 'gallery'

urlpatterns = [
    path('', views.GalleryIndex.as_view(), name='index'),
    path('macro/', views.MacroGallery.as_view(), name='macro'),
    path('paisajes/', views.PaisajeGallery.as_view(), name='paisajes'),
    path('fauna/', views.FaunaGallery.as_view(), name='fauna'),
    path('black_and_white/', views.BlackAndWhiteGallery.as_view(), name='black_and_white')
]
