from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from produto.views import ProdutoViewSet
from usuario.views import UsuarioViewSet, CompraViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register('produto', ProdutoViewSet, basename='Produto')
router.register('usuario', UsuarioViewSet, basename='Usuario')
router.register('compra', CompraViewSet, basename='Compra')

schema_view = get_schema_view(
    openapi.Info(
        title="Docs API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
