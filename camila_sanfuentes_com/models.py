from django.db import models


class MainPageContent(models.Model):
    about_me = models.TextField()
    portrait = models.ImageField(upload_to='main_page', null=True, blank=True, unique=True)
