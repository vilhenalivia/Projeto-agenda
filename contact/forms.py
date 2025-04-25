from django import forms
from django.core.exceptions import ValidationError
from . import models

# Criação de um form com base no nosso modelo
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'classe a classe b',
                'placeholder' : 'Escreva aqui'
            }
        ),
        help_text= 'Texto de ajuda para o usuário',
    )

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)

    #Informações relacionadas com o form
    class Meta:
        # Fomulario baseado no model Contacts
        model = models.Contact
        # Compos a serem listados no form
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category')

    
    # Dados limpos do formulário
    # Método clean tem acesso a todos os campos do formulario
    def clean(self):
        # cleaned_data = self.cleaned_data

        # #
        # self.add_error(
        #     'first_name', ValidationError('Mensagem de erro', code='invalid')
        # )

        return super().clean()
    
    # VALIDAÇÃO DO VALOR DO CAMPO -> clean campo
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        # Validação
        if first_name == 'ABC':
            self.add_error(
                'first_name', ValidationError('Mensagem de erro', code='invalid')
            )

        return first_name
        
    
