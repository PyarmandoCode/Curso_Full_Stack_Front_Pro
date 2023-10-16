datos = [100,200,300,500] #list
#Metodos propios
#Añadir elementos
datos.append(600) #Al Final de la Lista
datos.insert(1,790) #En la Posicion indicada
#Eliminar Elementos
datos.pop(3)#Por Su indice
datos.remove(100)#Por Su Valor
#Actualizar elemento
datos[2]=10000
#Recorrer Los Elementos de la Lista
# for x in datos:
#     print(x)
#Buscar un elemento de la Lista
# paises = ["El Salvador","Colombia","Ecuador","Panama"] #list
# valor = input("Ingresar Valor:")    
# if valor in paises:
#     print("Pais encontrado")
# else:
#     print("El Pais no existe se procedera a añadirlo")   
#     paises.append(valor) 
#     paises.sort()#ordena los valores de la lista
#     #paises.reverse()
#     print(paises)


#Diccionarios
empleados = {
             #KEY  - #VALOR
             "A100":"PEREZ",
             "A200":"GOMEZ",
             "A300":"TAPIA",
             "A400":"ROSALES",
             }

# print(empleados["A200"])
# print(empleados.keys())
# print(empleados.values())
# print(empleados.items())

personas = [
    {
        'nombre': 'Juan',
        'edad': 25,
        'ciudad': 'Madrid'
    },
    {
        'nombre': 'María',
        'edad': 30,
        'ciudad': 'Barcelona'
    },
    {
        'nombre': 'Pedro',
        'edad': 22,
        'ciudad': 'Valencia'
    }
]
#Acceder a los datos de la lista

for persona in personas:
    print(f"Nombre: {persona['nombre']}")
    print(f"Nombre: {persona['edad']}")
    print(f"Nombre: {persona['ciudad']}")
    print()