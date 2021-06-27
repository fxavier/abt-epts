from django.db import models
from core.models import Provincia, Distrito, UnidadeSanitaria


class Confidente(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    parentesco = models.CharField(max_length=100, blank=True, null=True)
    telefone1 = models.CharField(max_length=100, blank=True, null=True)
    telefone2 = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
class Paciente(models.Model):
    nid = models.CharField(max_length=100, unique=True, primary_key=True)
    genero = models.CharField(max_length=10)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateTimeField()
    telefone = models.CharField(max_length=100, blank=True, null=True)
    profissao = models.CharField(max_length=100, blank=True, null=True)
    nivel_escolaridade = models.CharField(max_length=100, blank=True, null=True)
    confidente = models.ForeignKey(Confidente, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nome} {self.nid}'
    
    
    
