from django.shortcuts import render
from .models import Vuelo,Pasajero

from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse



def index(request):
    template_name="index.html"
    context = {
        'vuelos':Vuelo.objects.all()
    }
    return render(request,template_name,context)

def vuelo(request,vuelo_id):
    template_name="vuelo.html"
    try:
        vuelo=Vuelo.objects.get(pk=vuelo_id)
        pasajeros=vuelo.pasajeros.all() #Pasajeros que se han registrado en ese vuelo
        no_pasajeros=Pasajero.objects.exclude(vuelo=vuelo).all() #Pasajeros que no se encuentran en ese vuelo
    except Vuelo.DoesNotExist:
        raise Http404("Vuelo No Existe")    
    context = {
        "vuelo":vuelo,
        "pasajeros":pasajeros,
        "no_pasajeros":no_pasajeros
    }
    return render(request,template_name,context)
    
    