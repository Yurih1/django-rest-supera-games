import uuid
from django.db import models
from produto.models import Produto


class Usuario(models.Model):
    
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('PNI', 'Prefiro nao informar')
    )
    
    id = models.CharField(primary_key=True, max_length=255, default=uuid.uuid4, unique=True)
    nome = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=255)
    sexo = models.CharField(max_length=20, choices=SEXO, default='PNI')
    
    def __str__(self):
        return self.nome


class Compra(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=uuid.uuid4, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Produto, on_delete=models.CASCADE)