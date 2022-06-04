from django.shortcuts import render

from web.models import Tarifas #Importo tarifas del modelo


# Create your views here.

def Home(request):
    #Creo una variable y uso el modelo para asignarle datos
    tarifas=Tarifas.objects.all() 

    #creo un diccionario con los datos a enviar
    diccionario={
        'tarifas':tarifas,
    } 

    return render(request, 'index.html',diccionario)


def Tarifa(request):
    return render(request, 'tarifas.html')