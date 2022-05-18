from django.urls import path
from .views import homeCLients, incluirCLients, listarCLients


urlpatterns = [
    path('', homeCLients, name='home'),
    path('incluir/', incluirCLients, name='include'),
    path('listar/', listarCLients, name='list'),
]