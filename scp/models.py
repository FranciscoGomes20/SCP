from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Chamado(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    upload = models.FileField(upload_to ='uploads/')
    data_criacao = models.DateTimeField(default=datetime.now())
    data_final = models.DateTimeField(blank=True, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, blank=True, null=True)
    setor = models.ForeignKey('Setor', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulo
