from django.db import models

from django.contrib.auth.models import AbstractBaseUser



class Cliente (AbstractBaseUser):
       

    rut = models.CharField(max_length=10, unique=True)

    direccion= models.CharField(max_length=50)  

    nombres=models.CharField(max_length=50)
                           
    password= models.CharField(max_length=50 , null=False )


    correo=models.EmailField( max_length=50)
                           
    telefono=models.IntegerField(max_length=50)
                           
    last_login= models.DateTimeField(null=True)
                           
    USERNAME_FIELD='rut'
    def __str__(self):
        return self.rut


class Contrato(models.Model):

    folio = models.BigAutoField(primary_key=True)
    
    descripcion =models.CharField(max_length=500)
    fecha= models.DateField()
    firmaCli= models.CharField(max_length=20)
    firmaEmp =models.CharField(max_length=20)
    

    def __str__(self):
        return self.folio   