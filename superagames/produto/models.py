from django.db import models
import uuid

class Produto(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=uuid.uuid4, unique=True)
    nome = models.CharField(max_length=80)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    score = models.IntegerField()
    nome_imagem = models.CharField(max_length=80, null=True, blank=True)
    
    def __str__(self):
        return self.nome
