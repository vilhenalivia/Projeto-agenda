from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from contact.forms import ContactForm
from contact.models import Contact

# View CREATE
@login_required(login_url='contact:login')
def create(request):
    # Monta a URL baseada no nome de uma view
    form_action = reverse('contact:create')

    # Verificação se a requisição é um POST -> envia dados
    if request.method == 'POST':
        # Cria um objerto de ContactForm com os dados que vieram do POST
        form = ContactForm(request.POST, request.FILES)

        # Pacotes de dados a ser enviado para o HTML
        context = {
            'form' : form , 
            'form_action' : form_action,
        }

        # Salvamento dos dados do formulário se ele for válido
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            # Redireciona o usuario para criar um novo usuário
            return redirect('contact:update',contact_id = contact.pk)


        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        # Instância do contact form
        'form' : ContactForm(),
        'form_action' : form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

# View UPDATE
@login_required(login_url='contact:login')
def update(request, contact_id):

    # Busca um contato no model Contact, que tenha o ID igual a contact_id e show = true
    contact = get_object_or_404(Contact, pk = contact_id, show=True, owner=request.user)

    # Monta a URL baseada no nome de uma view
    form_action = reverse('contact:update', args=(contact_id,))

    # Verificação se a requisição é um POST -> envia dados
    if request.method == 'POST':
        # Cria um objeto de ContactForm com os dados que vieram do POST e atualiza um contato ja existente
        form = ContactForm(request.POST, request.FILES, instance = contact)

        # Pacotes de dados a ser enviado para o HTML
        context = {
            'form' : form , 
            'form_action' : form_action,
        }

        # Salvamento dos dados do formulário se ele for válido
        if form.is_valid():
            contact = form.save()
            # Redireciona o usuario para criar um novo usuário
            return redirect('contact:update',contact_id=contact.pk)


        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        # Instância do contact form
        'form' : ContactForm(instance=contact),
        'form_action' : form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

# View DELETE
@login_required(login_url='contact:login')
def delete(request, contact_id):

    # Busca um contato no model Contact, que tenha o ID igual a contact_id e show = true
    contact = get_object_or_404(Contact, pk = contact_id, show=True, owner=request.user)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')


    return render( 
        request, 
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )