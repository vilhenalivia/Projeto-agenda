from django.shortcuts import render
from contact.models import Contact

# Create your views here.
def index(request):

    # Objeto novo de contato
    contacts = Contact.objects.all()

    # Transforma contato em um dicionário
    context = {'contacts' : contacts, }

    return render(request, 'contact/index.html', context)