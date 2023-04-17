from django.db import models


# Create your models here.

class Gallery(models.Model):
    title = models.CharField(null=False, blank=False, max_length=250)
    description = models.CharField(max_length=600, blank=True)
    gallery_top_image = models.ImageField(upload_to='gallery', null=True, blank=True)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    IMAGE_SIZES = [
        ('L', 'Large'),
        ('M', 'Medium'),
        ('S', 'Small'),
    ]
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=True, blank=False)
    image_file = models.ImageField(upload_to='gallery', null=False, blank=False)
    description = models.CharField(max_length=600, null=True, blank=True)
    thumbnail_size = models.CharField(max_length=1, choices=IMAGE_SIZES, default='S')
    carousel_image = models.BooleanField(default=False)

    def __str__(self):
        return self.title
