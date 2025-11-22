from django.urls import path
from .views import inicio, enviar_correo, habilidades, proyectos, contacto, experiencia, educacion, sobre_mi

urlpatterns = [
    path('', inicio, name='inicio'),
    path('/enviar_correo', enviar_correo, name='enviar_correo'),
    path('/habilidades', habilidades, name='habilidades'),
    path('/proyectos', proyectos, name='proyectos'),
    path('/contacto', contacto, name='contacto'),
    path('/experiencia', experiencia, name='experiencia'),
    path('/educacion', educacion, name='educacion'),
    path('/sobre_mi', sobre_mi, name='sobre_mi')
]