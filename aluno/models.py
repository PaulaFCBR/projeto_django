from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True, help_text='Entre com a Matricula do Aluno')
    nome = models.CharField(max_length=100, help_text='Informe p nome do Aluno')
    data_inicial = models.DateField('Informe a data de Matricula')
    data_fim = models.DateField(null=True,
                                blank=True,
                                default=timezone.now(),
                                help_text='Informe Data final do Aluno')
    def __str__(self):
        return f'{self.matricula} - {self.nome} - {self.data_inicial} - {self.data_fim}'  

