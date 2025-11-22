from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, 'menu/inicio.html')

def enviar_correo(request):
    if request.method == "POST":
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"De: {email}\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ["zaga1709@hotmail.com"],
            )
            messages.success(request, "¡Tu mensaje se envió correctamente! 😊")
        except Exception as e:
            messages.error(request, "Ocurrió un error al enviar tu mensaje. Inténtalo más tarde 😔")
        

        return redirect("inicio")

    return redirect("inicio")

def habilidades(request):
    return render(request, 'menu/habilidades.html')

def proyectos(request):
    return render(request, 'menu/proyectos.html')

def contacto(request):
    return render(request, 'menu/contacto.html')

def experiencia(request):
    return render(request, 'menu/experiencia.html')

def educacion(request):
    return render(request, 'menu/educacion.html')

def sobre_mi(request):
    return render(request, 'menu/sobre_mi.html')