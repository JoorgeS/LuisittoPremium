from django import forms
from django.forms import ModelForm
from .models import Cuentas,Usuario,Oferta

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','correo','telefono']

class OfertaForm(ModelForm):
    class Meta:
        model = Oferta
        fields = ['tipoCuenta','descuento','fechaOferta']

class CuentaForm(ModelForm):
    class Meta:
        model = Cuentas
        fields = ['nombreCuenta','precio','duracion']