from django.contrib import admin
from gallery.models import Gallery, GalleryImage

# Register your models here.

admin.site.register(Gallery)
admin.site.register(GalleryImage)


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
