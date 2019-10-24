from django.shortcuts import render, redirect
from django.http import HttpResponse
from Usuarios.forms import UsuarioForm
from Usuarios.models import Usuario


def index(request):
    return HttpResponse("Hola, buena tarde.")


def hola(request):
    return HttpResponse("Este es el metodo Hola")


def usuario_log(request):
    return HttpResponse("Aqui se va a loguear un usuario llamando al template de login")


def usuario_nuevo(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('index')

    else:
        form = UsuarioForm()
    return render(request, 'Usuario/Registrar.html', {'form': form})



