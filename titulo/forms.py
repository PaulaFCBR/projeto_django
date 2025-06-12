from django import forms

#classe formulario inclusao
class TituloForm(forms.Form):
    descricao = forms.CharField(max_length=100,
                                required=True, 
                                help_text='Informe o nome do Titulo')
    