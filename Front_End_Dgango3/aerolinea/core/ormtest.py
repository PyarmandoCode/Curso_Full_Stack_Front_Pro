#ORM =  "Object-Relational Mapping" (Mapeo Objeto-Relacional) 
"""
Es una Tecnica que se utiliza en el desarrollo de software para facilitar interaccion con la BD relacionales.
Ventajas
========
1.-Elimina la necesidad de escribir consultas SQL directamente desde el codigo de la aplicacion NO=SELECT,INSERT,UPDATE,DELETE
2.-Permite alos desarrolladores trabajar con objetos y clases del mismo lenguaje
3.-Si Migras a otra BD seguramente el codigo de tu aplicacion no sufrira cambios
Ejemplos
Java=Hibernate
C#=Entity Framework
NodeJS=Sequelize
Django=Querysets
4.-Codigo de tu aplicacion es mas Legible(Adminsitrar,Leer ,Dar Soporte)
"""

from django.shortcuts import render
from .models import Vuelo,Pasajero
from django.db.models import Sum,Avg

Vuelos=Vuelo.objects.all() #Todos Select * from Vuelo
vuelo= Vuelo.objects.get(pk=3) #Select * from Vuelo where id=3
vuelos_filtro=Vuelo.objects.filter(duracion=10)
vuelos_salvador=Vuelo.objects.filter(origen__contains="El Salvador")#Select * from Vuelo where duracion like '%El Salvador%'
    #***Insertar
insertar=Pasajero.objects.create(nombre="Nuevo",apellido="Nuevo")#Insert into Vuelo ("Nuevo","Nuevo")
    #***Borrar 
pasajero_delete=Pasajero.objects.get(pk=7) #Select * from Vuelo where id=7
pasajero_delete.delete()#Delete from where id=7
    #***Actualizar
pasajero_update=Pasajero.objects.get(pk=9) #Select * from Vuelo 
pasajero_update.nombre="NUEVO2"
pasajero_update.apellido="NUEVO2"
pasajero_update.save()


#Multiples Condiciones
objetos_filtrados=Vuelo.objects.filter(precio__gte=1900,duracion=22)

#Agrupar
total = Vuelo.objects.aggregate(Sum('precio'))
promedio = Vuelo.objects.aggregate(Avg('precio'))

#Select RAW
consulta_sql="Select * from core_vuelo where origen = 'El Salvador'"
resultados=Vuelo.objects.raw(consulta_sql)

for resultado in resultados:
    print(resultado)


    print(Vuelos)
    
    #print(f" total y promedio: {total} y el {promedio}")

