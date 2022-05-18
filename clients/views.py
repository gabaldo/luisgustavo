from django.shortcuts import render
from .models import Clients

# Create your views here.
def homeCLients(resquest):
    return render(resquest, 'clients/home.html')


def incluirCLients(resquest):
    return render(resquest, 'clients/incluir.html')


def listarCLients(resquest):
    clients = Clients.objects.all()
    print(clients)
    return render(resquest, 'clients/listar.html', {
        'clients': clients
    })