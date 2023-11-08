from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import MovieSerializer,PersonSerializer
from .models import Movie,Person

from django.contrib.auth.models import User #tabla user
from rest_framework.authtoken.models import Token #tabla token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
import json
from django.http import HttpResponse


class MovieAllViewset(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class PersonAllViewset(generics.ListAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

#Esta clase me genera un metodo RESTFULL
class MovieFullViewset(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    
class LoginView(APIView):

    def post(self,request):
        username=request.data["username"]
        password=request.data["password"]
        user=authenticate(username=username,password=password)
        if user:
            data = {
                "nombre":user.first_name,
                "apellido":user.last_name,
                "correo":user.email
            }
        else:
            data={"error":"Credenciales Invalidas"}    
        rpta=json.dumps(data) 
        return HttpResponse(rpta,content_type="application/json")   




        






    
    
