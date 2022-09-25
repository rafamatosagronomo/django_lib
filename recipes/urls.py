from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home, name='Bem vindo Cara'),
    path('sobre/', sobre, name='Sobre'),
    path('contato/', contato, name='Contato'),
]