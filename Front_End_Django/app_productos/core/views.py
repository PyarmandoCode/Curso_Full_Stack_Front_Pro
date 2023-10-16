from django.shortcuts import render

def index(request):
    #El Template que vas a renderizar
    template_name="index.html"

    return render(request,template_name)
    

def quienes(request):
    #El Template que vas a renderizar
    template_name="quienes.html"
    
    return render(request,template_name)