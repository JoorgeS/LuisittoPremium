from django.urls import path
from .views import lista_cuentas, detalle_cuenta
from .viewsLogin import login
urlpatterns =[
    path('lista_cuentas',lista_cuentas, name='lista_cuentas'),
    path('detalle_cuenta/<nombreCuenta>',detalle_cuenta, name="detalle_cuenta"),
    path('login',login,name="login_html"),
]