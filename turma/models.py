from django.db import models
from django.utils import timezone

from tiposdeatividade.models import TipoDeAtividade
from aluno.models import Aluno
from instrutor.models import Instrutor


# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text='Numero da turma')
    duracao = models.SmallIntegerField(help_text='Informe a duração da turma')
    horario_aula = models.TimeField(help_text='Informe o horario da aula')
    data_inicial = models.DateField(null=True,
                                    default=timezone.now(),
                                    help_text='Informe a data inicial da turma')
    data_final = models.DateField(null=True,
                                  blank=True,
                                  help_text='Informe a data final da turma')
    
    codigo_atividade= models.ForeignKey(TipoDeAtividade, null=True, blank=True,
                                        on_delete=models.CASCADE,
                                        related_name='atividades')
    matricula_monitor= models.ForeignKey(Aluno, null=True, blank=True,
                                        on_delete=models.SET_NULL,
                                        related_name='alunos')
    id_instrutor= models.ForeignKey(Instrutor, null=True, blank=True,  
                                        on_delete=models.CASCADE,
                                        related_name='instrutores')

    def __str__(self):
        return f'{self.numero} - {self.duracao} - {self.horario_aula} - {self.data_inicial} - {self.data_final}' 