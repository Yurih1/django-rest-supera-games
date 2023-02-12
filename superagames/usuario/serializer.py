from rest_framework import serializers
from usuario.models import Usuario, Compra

class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Compra
        exclude = []
