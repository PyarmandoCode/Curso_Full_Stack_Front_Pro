from django.db import models

class Driver(models.Model):
    name= models.CharField(max_length=30,null=True)
    license = models.CharField(max_length=30,null=True)

    def __str__(self) :
        return self.name

class Car(models.Model):
    make=models.CharField(max_length=30,null=True)
    model=models.CharField(max_length=30,null=True)
    year=models.IntegerField()
    vin=models.CharField(max_length=30,null=True)
    picture=models.CharField(max_length=130,null=True)
    owner=models.ForeignKey("Driver",on_delete=models.SET_NULL,null=True)

    def __str__(self) :
        return f"Marca:{self.make} y Modelo :{self.model}"




