from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(
        label="Nombre",
        max_length=100
    )
    email = forms.EmailField(
        label="Correo electrónico",
        max_length=100
    )
    message = forms.CharField(
        label="Mensaje"
    )

