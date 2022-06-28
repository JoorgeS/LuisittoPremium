from rest_framework import serializers
from Apps.models import Cuentas

class cuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentas
        fields = ['nombreCuenta','precio','duracion']
