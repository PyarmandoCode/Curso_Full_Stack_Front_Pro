class Productos:
    def __init__(self,nombre,precio,descripcion,fabricante,stock):
        self.nombre=nombre
        self.precio=precio
        self.descipcion=descripcion
        self.fabricante=fabricante
        self.stock=stock

    def mensaje_oferta(self):
        if self.precio>1000:
            print("El producto esta con oferta")
        else:
            print("No Tiene Oferta Aun")

    def consultar_stock(self):
        if self.stock<=0:
            print("Producto Sin Stock")        
        else:  
            print("Producto Con Stock")          
                

#Crear el Primer Objeto
libros=Productos("Aprende Python",100,"dddddd","SOPENA",100)
discos=Productos("SODA STEREO",200,"dddddd","SODA",0)
laptops=Productos("TOSHIBA",1200,"ddddddDDDD","TOSHIBA MR",900)
#Utilizar el Metodo
#laptops.mensaje_oferta()
#discos.mensaje_oferta()
discos.consultar_stock()



# print(libros.__dict__)#las propiedades del objeto
# print(discos.__dict__)
# print(laptops.__dict__)
# print(laptops.precio)#Mostrar el campo indicado
# print(laptops.nombre)