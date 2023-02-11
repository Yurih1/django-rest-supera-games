from django.db import models
import uuid


class Usuario(models.Model):
    
    SEXO = (
        ('Masculino', 'M'),
        ('Feminino', 'F'),
        ('Prefiro nao informar', 'PNI')
    )
    
    id = models.CharField(primary_key=True, max_length=255, default=uuid.uuid4, unique=True)
    nome = models.CharField(max_length=80)
    password = models.CharField(max_length=50)
    sexo = models.CharField(max_length=20, choices=SEXO, default='PNI')
    