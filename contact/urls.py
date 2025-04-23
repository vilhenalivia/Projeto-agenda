from django.urls import path
from contact import views

app_name = 'contact'

# Criação de uma nova url HTTP
urlpatterns = [
    # Caminho princial - vazio
    path('', views.index, name='index'), #type: ignore
     # Caminho para contato único - Pega como parametro um inteiro que seriao ID do contato
    # OBS: por padrão, sempre colocar uma barra final para não gerar problemas
    path('<int:contact_id>/', views.contact, name='contact'), #type: ignore
]