from django.db import models
from django.utils import timezone
# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True, help_text='Entre com a Matricula do Aluno')
    nome = models.CharField(max_length=100, help_text='Informe p nome do Aluno')
    data_inicial = models.DateField(null=False, default=timezone.now(),
                                    help_text='Informe a data de Matricula na escola')
    data_fim = models.DateField(null=True,
                                blank=True,
                                help_text='Informe Data final do Aluno na escola')
    def __str__(self):
        return f'{self.matricula} - {self.nome} - {self.data_inicial} - {self.data_fim}'  

