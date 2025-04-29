from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models


# Criação de um form com base no nosso modelo
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        )
    )

    #Informações relacionadas com o form
    class Meta:
        # Fomulario baseado no model Contacts
        model = models.Contact
        # Compos a serem listados no form
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',)

    
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
        
class RegisterForm(UserCreationForm):
    # Colocando campos em modo obrigátorio 
    first_name = forms.CharField( required=True, min_length=3)
    last_name = forms.CharField( required=True, min_length=3)
    email = forms.EmailField( required=True, min_length=3)

    
    #Configurar comportamentos internos do formulário
    class Meta:
        model = User # Modelo do formulário
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        ) # Campos que estarão no forms
    
    # Validar e limpar dados do formulário
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Se o user tiver o email já existente, aparecer uma mensagem de erro
        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Já existe este e-mail', code='invalid'))

        return email