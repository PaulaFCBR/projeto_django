from django.db import models

# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text='Numero da turma')
    duracao = models.SmallIntegerField(help_text='Informe a duração da turma')
    horario_aula = models.TimeField(help_text='Informe o horario da aula')
    data_inicial = models.DateField(help_text='Informe a data inicial da turma')
    data_final = models.DateField(help_text='Informe a data final da turma')
    
    def __str__(self):
        return f'{self.numero} - {self.duracao} - {self.horario_aula} - {self.data_inicial} - {self.data_final}' 