from rest_framework import viewsets
from usuario.models import Usuario, Compra
from usuario.serializer import UsuarioSerializer, CompraSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def get_queryset(self,):
        queryset = Usuario.objects.all()
        name = self.request.query_params.get('nome')
        password = self.request.query_params.get('password')

        if name and password:
            queryset = queryset.filter(nome=name, password=password)
        return queryset


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
