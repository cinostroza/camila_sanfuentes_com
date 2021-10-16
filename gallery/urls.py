from django.urls import path
from gallery.views import GalleryIndex

app_name = 'gallery'

urlpatterns = [
    path('', GalleryIndex.as_view(), name='index')
]