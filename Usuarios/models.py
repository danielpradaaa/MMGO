from django.db import models


class Usuario(models.Model):
    User_ID = models.CharField(primary_key=True, max_length=10)
    Nombre_Usuario = models.CharField(max_length=45)
    Username = models.CharField(max_length=45)
    Correo_Usuario = models.CharField(max_length=255)
    Password = models.CharField(max_length=32)
    Super_User = models.CharField(max_length=1)
    Direccion_Residencia = models.CharField(max_length=45)

