from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# View index
def index(request):

    # Objeto novo de contato chamado CONTACTS
    # Filtra os dados com Show = A true e ordens por Id decrescente
    contacts = Contact.objects.filter(show = True).order_by('-id')[0:10]

    # Transforma contato em um dicionário
    context = {'contacts' : contacts, }

    return render(request, 'contact/index.html', context)

# View contact
def contact(request, contact_id):

    # Objeto novo de contato chamado SINGLE_CONTACT
    # Filtra os dados com Show = A true e ordens por Id decrescente
    # GET -> retorna um único valor que seria a chave primária( ID do contato )
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id)

    # Transforma contato em um dicionário
    context = {'contact' : single_contact, }

    return render(request, 'contact/contact.html', context)