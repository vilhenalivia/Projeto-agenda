from django.urls import path
from . import views

app_name = 'contact'

# Criação de uma nova url HTTP
urlpatterns = [
    # Caminho princial - vazio
    path('', views.index, name='index'), #type: ignore

    # Caminho search no mesmo index
    path('search/', views.search, name='search'), 

    # CONTACT - (CRUD)
    # Caminho para contato único - Pega como parametro um inteiro que seria o ID do contato
    # OBS: por padrão, sempre colocar uma barra final para não gerar problemas
    path('contact/<int:contact_id>/', views.contact, name='contact'), #type: ignore
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # USER (CRU)
    path('user/register/', views.register, name="register"),
    path('user/login/', views.login_view, name="login"),
    path('user/logout/', views.logout_view, name="logout"),
    path('user/update/', views.user_update, name="user_update"),
]