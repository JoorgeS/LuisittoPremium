from django.http import request
from django.shortcuts import render, redirect
from .models import Cuentas, Usuario, Oferta
from .forms import CuentaForm, OfertaForm, UsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
class Usuario:
    def __init__(self,nombre,correo,telefono, clave):
        self.nombre = nombre
        self.correo=correo
        self.telefono=telefono

        super(). __init__()
        
# Create your views here.

def index(request):

    return render(request, "core/index.html")
def contacto(request):


    return render(request, "core\contacto.html" )

def login(request):


    return render(request, "core\login.html" )
def ofertas(request):
    listaCuentas = Cuentas.objects.all()
    datos= {
        'Cuentas': listaCuentas
        
    }


    return render(request, "core\ofertas.html", datos )
    
def registro(request):


    return render(request, "core/registro.html" )

def Somos(request):


    return render(request, "core/Somos.html" )

def TyC(request):


    return render(request, "core\TyC.html" )
@login_required
def agregarCuenta(request):
    datos = {
        'form' :  CuentaForm()
    }

    if (request.method == 'POST'):
        formulario = CuentaForm(request.POST)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            messages.success(request, "modificado Correctamente")
            datos['mensaje'] = 'Cuenta se guardó'
        else:
            datos['mensaje'] = 'Cuenta NO se guardó'
            messages.error(request, "No se pudo agregar")
  
    return render(request,'core/agregarCuenta.html', datos)

@login_required
def modificarCuenta(request, nombreCuenta):
    cuenta = Cuentas.objects.get(nombreCuenta=nombreCuenta) #select * from Cuentas where nombre = id

    datos = {
        'form': CuentaForm(instance=cuenta)
    }
    if (request.method == 'POST'):
        formulario = CuentaForm(data=request.POST, instance=cuenta)
        if formulario.is_valid():
            formulario.save() #modificar a la BD
            messages.success(request, "modificado Correctamente")
            datos['mensaje'] = 'Cuenta se modificó'
        else:
            datos['mensaje'] = 'cuenta NO se modificó'
            messages.error(request, "No se pudo modificar")
    return render(request,'core/modificarCuenta.html', datos)
@login_required
def eliminarCuenta(request, nombreCuenta):
    cuentas = Cuentas.objects.get(nombreCuenta=nombreCuenta)
    cuentas.delete() # delete from Vehiculo where nombre = id
    messages.success(request, "modificado Correctamente")

    return redirect(to='ofertas')

