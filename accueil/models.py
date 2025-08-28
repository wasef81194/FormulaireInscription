from django.db import models

# Create your models here.
class Visiteur(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom