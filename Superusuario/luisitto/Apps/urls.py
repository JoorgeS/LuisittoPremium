from django.urls import path
from .views import eliminarCuenta, index, contacto, login, modificarCuenta, ofertas, registro,Somos,TyC,agregarCuenta,modificarCuenta, eliminarCuenta

urlpatterns =[
    path('', index, name="index"),
    path('contacto', contacto, name="contacto"),
    path('login', login, name="login"),
    path('ofertas', ofertas, name="ofertas"),
    path('registro', registro, name="registro"),
    path('Somos', Somos, name="Somos"),
    path('TyC', TyC, name="TyC"),
    path('agregarCuenta',agregarCuenta,name="agregarCuenta"),
    path('modificarCuenta/<nombreCuenta>',modificarCuenta,name="modificarCuenta"),
    path('eliminarCuenta/<nombreCuenta>',eliminarCuenta,name="eliminarCuenta"),
]