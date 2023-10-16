#Condicionales Simples
edad= 18
if edad>18:
    print("Es Mayor de edad")#Bloque de codigo True
else:
    print("Es Menor de edad")#Bloque de codigo False    

#Condicionales Multiples
if edad>=2 and edad<=5:
    print("Es Un Niño")
elif edad>=6 and edad<=15:   
    print("Es Un Adolecente")
elif edad>=16 and edad<=28:   
    print("Es Un Joven")
else:
    print("Es Un Adulto")    

"""
Y = AND
O = OR
Diferente => !=
Negacion = NOT
Igual => "=="

"""    
#Ejemplo de Case

def obtener_dia(opcion):
    #indent
    switch = {
        0:"Domingo",
        1:"Lunes",
        2:"Martes",
        3:"Miercoles",
        4:"Jueves",
        5:"Viernes",
        6:"Sabado"
    } 
    return switch.get(opcion,"Dia Invalido")

#print(obtener_dia(3))

#Bucles
#For
for x in range(1,10,2):
   print(f"{x} Hola Mundo")
#While

contador=1
while contador <=10:#True
    if contador ==5:
        break #Salir del bucle
    print(contador)
    contador +=1 #Aumentar el bucle
print("Fuera del Bucle")     


contador=1
while contador <=10:#True
    if contador ==5:
        contador +=1 #Aumentar el bucle
        continue #Saltar la iteraccion cuando el contador sea 5
    print(contador)
    contador +=1
print("Fuera del Bucle")     

