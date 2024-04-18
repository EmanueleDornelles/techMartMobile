from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/',DetailProdutos.as_view()),
    path('',ListProdutos.as_view()),
    path('create/',CreateProdutos.as_view()),
    path('delete<int:pk>/',DeleteProdutos.as_view())
]