from django.db import models
from django.utils import timezone
from django.urls import reverse
from django_editorjs_fields import EditorJsJSONField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250, null=False)
    body = EditorJsJSONField(readOnly=False, autofocus=True, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=150)
    post_header_image = models.ImageField(upload_to='blog_images', null=True)

    def publish(self):
        self.date = timezone.now()
        self.save()

    # def approve_comment(self):
    #     return self.comment.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
