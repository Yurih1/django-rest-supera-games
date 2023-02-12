from django.contrib import admin
from produto.models import Produto
from usuario.models import Usuario

class Produtos(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'score', 'nome_imagem')
    list_display_links = ('nome',)
    list_per_page = 50
    search_fields = ('nome', 'score',)

admin.site.register(Produto, Produtos)
