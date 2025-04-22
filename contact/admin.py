from django.contrib import admin
from contact import models

# Register your models here.

# Configuração do seu model admin no django
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Aparecer no display
    list_display = 'id','first_name', 'last_name', 'phone',
    # Ordernar por ID decrescente 
    ordering = '-id',   
    # Adiciona o campo de pesquisa
    search_fields = 'id', 'first_name', 'last_name'
    # Listar uma quantidade de valores por pagina
    list_per_page =  10
    # Maximo de valores que podem ser apresentados em mostrar tudo
    list_max_show_all = 100

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)
    

