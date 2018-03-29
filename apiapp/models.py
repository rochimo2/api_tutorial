from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    deseo = models.CharField(max_length=255, blank=False, unique=True)
    dueño = models.ForeignKey(
        'auth.User',
        related_name='bucketlists',
        on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

# This receiver handles token creation when a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

