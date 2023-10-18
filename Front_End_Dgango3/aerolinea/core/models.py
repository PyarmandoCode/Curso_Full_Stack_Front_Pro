from django.db import models

class Vuelo(models.Model):
    origen=models.CharField(max_length=64)
    destino=models.CharField(max_length=64)
    duracion=models.IntegerField(null=True)
    precio=models.DecimalField(max_digits=7,decimal_places=2)
    descripcion=models.TextField(blank=True,null=True)
    foto = models.ImageField(upload_to='vuelos',blank=True,null=True)

    def __str__(self) :
        return f"{self.id} - {self.origen} Hasta {self.destino}"
    
    class Meta:
        ordering = ['id']



