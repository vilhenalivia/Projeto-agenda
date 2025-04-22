from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#ID -> Primary key -> Gerado automaticamente
class Category(models.Model):
    # Retorna ao nome Categorias em muito itens ou categoria em uma
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=50)

    #Mostrar o nome 
    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    # Primeiro nome em maximo de 50 caracteres obrigatório
    first_name = models.CharField(max_length=50)
    # Fim do nome em maximo de 50 caracteres opcional
    last_name = models.CharField(max_length=50, blank=True)
    # Telefone com maximo de 50 caracters obrigatório
    phone = models.CharField(max_length=50)
    # Email com maximo de 254 caracteres opcional
    email = models.EmailField(max_length=254, blank= True)
    # Data de criação criada automaticamente sem edição
    created_date = models.DateTimeField(default= timezone.now)
    # Descrição de texto de modo opcional
    description = models.TextField(blank=True)
    # Quer ou não exibir o contato
    show = models.BooleanField(default=True)
    # Adicionar uma imagem sem obrigátoriedade
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    # Chave estrangeira, en caso de deletar a categoria, aparecer com vazio, com a permição de ser vazio
    category = models.ForeignKey(
        Category, # Da classe Category
        on_delete=models.SET_NULL,  # O que acontece quando o objeto é deletado, ou seja, será vazio, mas aainda existirá o contato
        blank=True, null=True) # Com permisão de ser vazio
    # Owner - Foreing key
    owner = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        blank=True, null=True
    )


    # Retorna a escrita do primeiro e segundo nome da pessoa
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
