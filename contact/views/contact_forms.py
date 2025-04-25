from django.shortcuts import render, redirect

from contact.forms import ContactForm

# View CREATE
def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            # Instância do contact form
            'form' : ContactForm(request.POST)
        }

        # Salvamento dos dados do formulário se ele for válido
        if form.is_valid():
            form.save()
            # Redireciona o usuario para criar um novo usuário
            return redirect('contact:create')


        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        # Instância do contact form
        'form' : ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )