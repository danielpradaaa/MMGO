from django import forms
from Usuarios.models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'Username',
            'Password',
            'User_ID',
            'Nombre_Usuario',
            'Correo_Usuario',
            'Super_User',
            'Direccion_Residencia',
        ]

        labels = {
            'Username': 'Usuario de acceso',
            'Password': 'Contraseña de acceso',
            'User_ID': 'Cédula',
            'Nombre_Usuario': 'Nombre completo',
            'Correo_Usuario': 'Correo electrónico',
            'Super_User': '¿Es super usuario?',
            'Direccion_Residencia': 'Dirección de residencia',
        }

        widgets = {
            'Username': forms.TextInput(),
            'Password': forms.TextInput(),
            'Username': forms.TextInput(),
            'Password': forms.TextInput(),
            'User_ID': forms.TextInput(),
            'Nombre_Usuario': forms.TextInput(),
            'Correo_Usuario': forms.TextInput(),
            'Super_User': forms.TextInput(),
            'Direccion_Residencia': forms.TextInput(),
        }
