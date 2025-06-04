from django.db import models

# Create your models here.
class Instrutor(models.Model):
    id = models.AutoField(primary_key=True, help_text='ID do instrutor')
    rg = models.CharField(max_length=15, help_text='Informe o RG do Instrutor')
    nome = models.CharField(max_length=100, help_text='Informe p nome do Instrutor')
    data_nascimento = models.DateField(help_text='Informe a data de nascimento')
    telefone = models.CharField(max_length=9, help_text='Informe o telefone do Instrutor')
    ddd = models.CharField(max_length=3, help_text='Informe o DDD do Instrutor')
    
    def __str__(self):
        return f'{self.id} - {self.nome} - {self.rg} - {self.data_nascimento} - {self.telefone} - {self.ddd}' 