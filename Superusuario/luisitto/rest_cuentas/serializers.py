from rest_framework import serializers
from Apps.models import Cuentas

Class cuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentas
        fields = ['nombreCuenta','precio','duracion']
