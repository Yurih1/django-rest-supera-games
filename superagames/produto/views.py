from rest_framework import viewsets
from produto.models import Produto
from produto.serializer import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_queryset(self,):
        queryset = Produto.objects.all()
        alphabetical = self.request.query_params.get('alfabetica')
        popularity = self.request.query_params.get('popularidade')

        if alphabetical:
            queryset = Produto.objects.order_by('nome')
            
        elif popularity:
            set_score = '-score' if popularity == 'true' else 'score'
            queryset = Produto.objects.order_by(set_score)

        return queryset
