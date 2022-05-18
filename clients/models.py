from django.db import models

# Create your models here.
class Clients(models.Model):
    nome = models.CharField(max_length=30)
    matricula = models.CharField(max_length=7)

    def __str__(self):
        return self.nome
