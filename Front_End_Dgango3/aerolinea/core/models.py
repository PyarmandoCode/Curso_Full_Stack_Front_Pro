from django.db import models

class Vuelo(models.Model):
    origen=models.CharField(max_length=64)
    destino=models.CharField(max_length=64)
    duracion=models.IntegerField(null=True)
    precio=models.DecimalField(max_digits=7,decimal_places=2)
    descripcion=models.TextField(blank=True,null=True)
    foto = models.ImageField(upload_to='vuelos',blank=True,null=True)

    def __str__(self) :
        return f"{self.origen} - {self.destino}"
    
    class Meta:
        ordering = ['id']

class Pasajero(models.Model):
    nombre=models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    vuelo=models.ManyToManyField(Vuelo,blank=True,related_name="pasajeros")
    foto = models.ImageField(upload_to='vuelos',blank=True,null=True)
    info=models.TextField(null=True,blank=True)

    def __str__(self) :
        return f"{self.nombre} - {self.apellido}"



