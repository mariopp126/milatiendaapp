# tienda/views.py

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Producto, Opiniones
from .forms import ContactForm, OpinionForm

def home(request):
    if request.method == 'POST':
        if 'sumbit_contact' in request.POST:
            contact_form = ContactForm(request.POST)
            opinion_form = OpinionForm()
            if contact_form.is_valid():
                # Guardar los datos del formulario
                name = contact_form.cleaned_data['name']
                email = contact_form.cleaned_data['email']
                message = contact_form.cleaned_data['message']
                
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
            
        elif 'submit_opinion' in request.POST:
            opinion_form  = OpinionForm(request.POST)
            contact_form = ContactForm()
            
            if opinion_form .is_valid():
                
                if opinion_form .save():
                    success_message_opinion = "¡Tu mensaje ha sido enviado con éxito!"
                    
                else:
                    success_message_opinion = "¡Hubo un error al enviar el formulario!"
                    
            else:
                success_message_opinion = "¡Revisa los campos ingresados y vuelve a intentarlo!"
                
            return render(request, 'home.html', {'success_message_opinion': success_message_opinion})
                
    else:
        contact_form = ContactForm()
        opinion_form = OpinionForm()
        
    return render(request, 'home.html', {
        'contact_form': contact_form,
        'opinion_form': opinion_form
    })

""" def save_opinion(request):
    if request.method == 'POST':
        formOpinion = OpinionForm(request.POST)
        if formOpinion.is_valid():
            formOpinion.save()
            return redirect('home.html') 
    else:
        formOpinion = OpinionForm()
    return render(request, 'home.html', {'fields': formOpinion}) """

