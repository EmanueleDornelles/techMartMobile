from rest_framework import serializers
from .models import *

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id','NomeProduto','Descricao','Preco','Estoque')