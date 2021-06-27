from django.db import models
from core.models import Provincia, Distrito, UnidadeSanitaria
from patients.models import Paciente


class SituacaoFamilia(models.Model):
    nome = models.CharField(max_length=150)
    parentesco = models.CharField(max_length=100)
    idade = models.IntegerField()
    teste_hiv = models.CharField(max_length=100)
    cuidados_hiv = models.CharField(max_length=100)
    em_ccr = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class CuidadosHiv(models.Model):
    teste_hiv_pos = models.CharField(max_length=100)
    data = models.DateTimeField()  
    local = models.CharField(max_length=100)
    diagnostico_pr_criancas = models.CharField(max_length=100)
    data_diagnostico = models.DateTimeField()  
    data_inicio_pre_tarv = models.DateTimeField()
    unidade_sanitaria_inicio = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    transferido_de = models.CharField(max_length=100)
    
    

class FichaResumo(models.Model):
    data_abertura = models.DateTimeField()  
    unidade_sanitaria = models.ForeignKey(UnidadeSanitaria, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
