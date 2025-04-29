from django.contrib import messages
from django.shortcuts import render, redirect

from contact.forms import RegisterForm


# Criação de uma VIEW de um  forms de registro de usuário
def register(request):
    form = RegisterForm()

    # Formulário de registro
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')

    return render (
        request,
        'contact/register.html',
        {
            'form': form
        }
    )