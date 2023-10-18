from django.shortcuts import render
from .models import Vuelo


def index(request):
    template_name="index.html"
    context = {
        'vuelos':Vuelo.objects.all()
    }
    return render(request,template_name,context)