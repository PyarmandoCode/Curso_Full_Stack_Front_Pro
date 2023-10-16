"""
*************************
Comentarios
Varias Lineas -DocString
*************************
"""
from datetime import datetime #Trabajar con fechas

#Tipo de datos Primitivos
nombre_curso='Full_Stack' #str
costo_curso=1200.90 #float
asistentes=20 #int
activo=True #bool
actual=datetime.now()#La fecha y hora actual del sistema
print(actual)
print(actual.date())
print(actual.time())


# print(type(nombre_curso))
# print(type(costo_curo))
# print(type(asistentes))
# print(type(activo))

#Concatenacion
#print(f"La Fecha de hoy es {actual.date()} y la hora es {actual.time()}")
#print(f"El Nombre del curso es {nombre_curso} y el costo es {costo_curso}")

numero=123.456789

#Formatear con dos decimales
cadena_formateada="{:.3f}".format(numero)
numero_formateado=f"{numero:.2f}"
print(numero_formateado)
