from django.http import request
from django.shortcuts import render, redirect
from .models import Cuentas, Usuario, Oferta
from .forms import CuentaForm, OfertaForm, UsuarioForm


class Usuario:
    def __init__(self,nombre,correo,telefono):
        self.nombre = nombre
        self.correo=correo
        self.telefono=telefono
        super(). __init__()
        
# Create your views here.
def index(request):
    listaCuentas = Cuentas.objects.all()
    datos= {
        'Cuentas': listaCuentas
        
    }
    return render(request, "core/index.html", datos )

def contacto(request):


    return render(request, "core\contacto.html" )


def login(request):


    return render(request, "core\login.html" )

def ofertas(request):
    Usuario =["Jaime","luisolivares@gmail.com","990002300"]


    return render(request, "core\ofertas.html" )
    

def registro(request):


    return render(request, "core/registro.html" )

def Somos(request):


    return render(request, "core/Somos.html" )

def TyC(request):


    return render(request, "core\TyC.html" )
def agregarCuenta(request):
    datos = {
        'form' :  CuentaForm()
    }

    if (request.method == 'POST'):
        formulario = CuentaForm(request.POST)
        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Cuenta se guardó'
        else:
            datos['mensaje'] = 'Cuenta NO se guardó'
  
    return render(request,'core/agregarCuenta.html', datos)

def modificarCuenta(request, nombreCuenta):
    cuenta = Cuentas.objects.get(nombreCuenta=nombreCuenta) #select * from vehiculo where patente = id

    datos = {
        'form': CuentaForm(instance=cuenta)
    }
    if (request.method == 'POST'):
        formulario = CuentaForm(data=request.POST, instance=cuenta)
        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'Cuenta se modificó'
        else:
            datos['mensaje'] = 'cuenta NO se modificó'
    return render(request,'core/modificarCuenta.html', datos)

def eliminarCuenta(request, nombreCuenta):
    cuentas = Cuentas.objects.get(nombreCuenta=nombreCuenta)
    cuentas.delete() # delete from Vehiculo where patente = id

    return redirect(to='index')





