from django.shortcuts import render


def index(request):
    """
    Vista simple que renderiza la hoja de vida estática de Diery.
    No realiza consultas a base de datos ni lógica compleja.
    """
    return render(request, 'Diery/index.html')
