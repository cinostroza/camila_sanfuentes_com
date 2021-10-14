from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.email

