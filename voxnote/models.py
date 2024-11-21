from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Note(models.Model):# modèle de Note pour les utilisateurs étant connectés
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("voxnote-detail", kwargs={"pk":self.pk} )

class Message(models.Model):# modèle de Message pour les utilisateurs n'étant pas connectés
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)