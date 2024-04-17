from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ListProdutos(generics.ListAPIView):             #Read
    queryset=Produto.objects.all()
    serializer_class=ProdutosSerializer

class DetailProdutos(generics.ListAPIView):          #Update
    queryset=Produto.objects.all()
    serializer_class=ProdutosSerializer

class CreateProdutos(generics.ListAPIView):          #Create
    queryset=Produto.objects.all()
    serializer_class=ProdutosSerializer

class DeleteProdutos(generics.ListAPIView):          #Delete
    queryset=Produto.objects.all()
    serializer_class=ProdutosSerializer

    
