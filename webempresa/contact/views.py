from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm
# Create your views here.


def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # Enviamo sel correo y redureccionamos
            email = EmailMessage(
                "La caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió\n\n{}".format(name, email, content),
                settings.EMAIL_HOST_USER,
                ["cesarmoraleslp@gmail.com"]
            )
            try:
                #todo ha ido bien, redireccionamos a OK
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    return render(request, "contact/contact.html", {'form':contact_form})