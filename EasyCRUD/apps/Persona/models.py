from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellido = models.CharField(max_length = 200, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)

    def __str__(self):
        return self.nombre