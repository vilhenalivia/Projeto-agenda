from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from contact.forms import RegisterForm, RegisterUpdateForm


# VIEW DE REGISTRO DE USUÁRIO
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


def user_update(request):
    form = RegisterUpdateForm(instance= request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contact:user_update')


# VIEW LOGIN
def login_view(request):
    # Fomulário de autenticação
    form = AuthenticationForm(request)

    # Se o for POST apresentar:
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        # Se o formulário for válido:
        if form.is_valid():
            # Recolher o usuário
            user = form.get_user()
            # Autenticação de login
            auth.login(request, user)
            # Mensagem de sucesso
            messages.success(request, 'Logado com sucesso!')
            # Retornar a página principal
            return redirect('contact:index')
        #Se não, mensagem de erro
        messages.error(request, 'Login Inválido')

    return render (
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

# VIEW LOGOUT   
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')