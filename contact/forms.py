from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

from . import models


# Criação de um form com base no nosso modelo
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        ),
        required=False
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
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2'] # Campos que estarão no forms
    
    # Validar e limpar dados do formulário
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Se o user tiver o email já existente, aparecer uma mensagem de erro
        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Já existe este e-mail', code='invalid'))

        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={ 'min_length':'Please, add more than 2 letters'}
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30, 
        required=False,
        help_text='Required'
    )
    password1 = forms.CharField(
        label='Password', 
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Use the same password as before.',
        required=False
    )

    #Configurar comportamentos internos do formulário
    class Meta:
        model = User # Modelo do formulário
        fields = ['first_name', 'last_name', 'email', 'username'] # Campos que estarão no forms
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()


    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password1')
    
        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', ValidationError('Senha não combinam'))

        return super().clean()

    # Validar e limpar dados do formulário
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            # Se o user tiver o email já existente, aparecer uma mensagem de erro
            if User.objects.filter(email=email).exists():
                self.add_error('email', ValidationError('Já existe este e-mail', code='invalid'))

        return email
    
    # Validação de senha
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if not password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))

        return password1