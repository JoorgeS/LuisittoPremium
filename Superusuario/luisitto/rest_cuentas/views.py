from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Apps.models import Cuentas
from rest_cuentas.serializers import cuentaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_cuentas(request):
    if request.method == 'GET':
        listaCuentas = Cuentas.objects.all()
        serializ = cuentaSerializer(listaCuentas, many = True)
        return Response(serializ.data)
    elif request.method == 'POST':
        dataV = JSONParser().parse(request)
        serializ = cuentaSerializer(data = dataV)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializ.errors, status = status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_cuenta(self, request, nombreCuenta):
        serializ = cuentaSerializer(listaCuentas, many = True)
        listaCuentas = list(nombreCuenta.objects.filter(nombreCuenta=nombreCuenta).values())
        if len(Cuentas) > 0:
            Cuentas = Cuentas.objects.get(nombreCuenta=nombreCuenta)
            Cuentas.nombreCuenta = serializ['nombreCuenta']
            Cuentas.precio = serializ['precio']
            Cuentas.duracion = serializ['duracion']
            serializ.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return Response(serializ.data)
