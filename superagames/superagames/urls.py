from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from produto.views import ProdutoViewSet
from usuario.views import UsuarioViewSet, CompraViewSet

router = routers.DefaultRouter()
router.register('produto', ProdutoViewSet, basename='Produto')
router.register('usuario', UsuarioViewSet, basename='Usuario')
router.register('compra', CompraViewSet, basename='Compra')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
