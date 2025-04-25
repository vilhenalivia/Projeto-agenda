from django.shortcuts import render

from contact.forms import ContactForm

# View CREATE
def create(request):
    if request.method == 'POST':
        context = {
            # Instância do contact form
            'form' : ContactForm(request.POST)
        }
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