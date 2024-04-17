from django.db import models

# Create your models here.

class Produto(models.Model):
    NomeProduto = models.CharField(max_length=100, blank=False)
    Descricao= models.TextField(blank=True)
    Preco = models.FloatField()
    Estoque = models.FloatField()
    

    def __str__(self):
        return self.NomeProduto


