from django import forms
from django.core.exceptions import ValidationError
from . import models

# Criação de um form com base no nosso modelo
class ContactForm(forms.ModelForm):
    #Informações relacionadas com o form
    class Meta:
        # Fomulario baseado no model Contact
        model = models.Contact
        # Compos a serem listados no form
        fields = ('first_name', 'last_name', 'phone')
    
    # Dados limpos do formulário
    def clean(self):
        # cleaned_data = self.cleaned_data
        
        self.add_error(
            'first_name', ValidationError('Mensagem de erro', code='invalid')
        )

        return super().clean()
    
