from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Status")
        verbose_name_plural = ("Status")
    
    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Setor")
        verbose_name_plural = ("Setores")

    def __str__(self):
        return self.nome

class Chamado(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    upload = models.FileField(upload_to ='uploads/', blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_final = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='usuario', on_delete=models.CASCADE, blank=True, null=True)
    funcionario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='funcionario', on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, blank=True, null=True)
    setor = models.ForeignKey('Setor', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = ("Chamado")
        verbose_name_plural = ("Chamados")

    def __str__(self):
        return self.titulo
