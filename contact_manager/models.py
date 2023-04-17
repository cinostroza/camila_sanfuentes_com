from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.email


class ContactRequest(models.Model):
    email = models.EmailField(null=True, blank=True)
    topic = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
