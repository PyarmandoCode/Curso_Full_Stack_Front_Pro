from django.shortcuts import render
from .models import Car,Driver,Feedback

def index(request):
    cars=Car.objects.all()#Trae la data
    context = {
        "c":cars
    }
    template_name="index.html"
    return render(request,template_name,context)

def driver_car(request,pk):
    try:
        driver=Driver.objects.get(pk=pk)
        feedbacks=Feedback.objects.filter(driver=1)
    except Driver.DoesNotExist:
        driver=None    
    context = {
        "d":driver,
        "f":feedbacks
    }
    template_name="driver.html"
    return render(request,template_name,context)
    


