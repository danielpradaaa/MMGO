from django.conf.urls import url
from Usuarios.views import index, hola, usuario_log, usuario_nuevo

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^hola', hola),
    url(r'^usuario_log', usuario_log),
    url(r'^usuario_nuevo', usuario_nuevo),
]