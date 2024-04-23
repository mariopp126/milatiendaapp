# tienda/views.py

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Producto, Opiniones
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar los datos del formulario
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Aquí podrías guardar los datos en un modelo si es necesario
            # Contact.objects.create(name=name, email=email, message=message)

            # Enviar un correo electrónico
            send_mail(
                subject='Nuevo contacto desde la página web',
                message=f"De: {name}\nEmail: {email}\nMensaje:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )
            success_message = "¡Tu mensaje ha sido enviado con éxito!"
            return render(request, 'home.html', {'success_message': success_message})
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def opiniones(request):
    opiniones = Opiniones.objects.all()
    return render(request, 'opiniones.html', {'opiniones': opiniones})

