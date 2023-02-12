from django.forms import ModelForm, PasswordInput
from usuario.models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'password': PasswordInput(),
        }
        