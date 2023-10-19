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
        no_pasajeros=Pasajero.objects.exclude(vuelo=vuelo).all() 
        #pasajeros_foto=Pasajero.objects.all()
        #Pasajeros que no se encuentran en ese vuelo
    except Vuelo.DoesNotExist:
        raise Http404("Vuelo No Existe")    
    context = {
        "vuelo":vuelo,
        "pasajeros":pasajeros,
        "no_pasajeros":no_pasajeros
    }
    
    return render(request,template_name,context)

def reservar(request,vuelo_id):
    try:
        pasajero_id=int(request.POST["pasajero"])
        pasajero=Pasajero.objects.get(pk=pasajero_id)
        vuelo=Vuelo.objects.get(pk=vuelo_id)
    except KeyError:
        return render(request,"error.html",{"msg":"No Selecciono el Pasajero"})
    except Vuelo.DoesNotExist:
        return render(request,"error.html",{"msg":"No Existe el Vuelo"})
    except Pasajero.DoesNotExist:
        return render(request,"error.html",{"msg":"No Existe el Pasajero"})
    #Adicionamos Un Vuelo al Pasajero seleccionado
    pasajero.vuelo.add(vuelo)
    #Se recargar toda la pagina se observara el pasajero ya incluido en ese vuelo
    return HttpResponseRedirect(reverse("vuelo",args=(vuelo_id,)))

    



    
    