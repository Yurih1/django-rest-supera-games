from django.contrib import admin
from usuario.form import UsuarioForm
from usuario.models import Usuario
class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioForm

admin.site.register(Usuario, UsuarioAdmin)
