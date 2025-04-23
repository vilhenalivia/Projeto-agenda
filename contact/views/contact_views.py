# Importa algo para deixar usar o OU em uma query
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact


# View index
def index(request):

    # Objeto novo de contato chamado CONTACTS
    # Filtra os dados com Show = A true e ordens por Id decrescente
    contacts = Contact.objects.filter(show = True).order_by('-id')[10:20]

    # Transforma contato em um dicionário
    context = {'contacts' : contacts, }

    return render(request, 'contact/index.html', context)

# View search
def search(request):

    # Pega o valor inserido pelo usuario sem contar espaços e coloca na variavel (search_value)
    search_value = request.GET.get('q', '').strip()

    # Se o valor dado em SEARCH for vazio, redireciona a pessoa até a pagina principal -> index
    if search_value == '':
        return redirect('contact:index')

    # Objeto novo de contato chamado CONTACTS
    # Filtra os dados com Show = A true e ordens por Id decrescente
    contacts = Contact.objects \
        .filter(show = True)\
        .filter(
            Q(first_name__icontains=search_value) | 
            Q(last_name__icontains= search_value) |
            Q(phone__icontains=search_value) | 
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    # Transforma contato em um dicionário
    context = {
        'contacts' : contacts , 
        'site_title': 'Search - '
    }

    return render(request, 'contact/index.html', context)


# View contact
def contact(request, contact_id):

    # Objeto novo de contato chamado SINGLE_CONTACT
    # Filtra os dados com Show = A true e ordens por Id decrescente
    # GET -> retorna um único valor que seria a chave primária( ID do contato )
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    # Transforma contato em um dicionário
    context = {
        'contact' : single_contact,
        'site_title' : site_title
    }

    return render(request, 'contact/contact.html', context)


