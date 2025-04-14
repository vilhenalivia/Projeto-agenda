from django.db import models
from django.utils import timezone
# Create your models here.


#ID -> Primary key -> Gerado automaticamente

class Contact(models.Model):
    # Primeiro nome em maximo de 50 caracteres obrigatório
    first_name = models.CharField(max_length=50)
    # Fim do nome em maximo de 50 caracteres opcional
    last_name = models.CharField(max_length=50, blank=True)
    # Telefone com maximo de 50 caracters obrigatório
    phone = models.CharField(max_length=50)
    # Email com maximo de 254 caracteres opcional
    emai = models.EmailField(max_length=254, blank= True)
    # Data de criação criada automaticamente sem edição
    created_date = models.DateTimeField(default= timezone.now)
    # Descrição de texto de modo opcional
    description = models.TextField(blank=True)
    # Quer ou não exibir o contato
    show = models.BooleanField(default=True)
    # Adicionar uma imagem sem obrigátoriedade
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')

    # Retorna a escrita do primeiro e segundo nome da pessoa
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
