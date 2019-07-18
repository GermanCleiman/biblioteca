from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank= False, null = False)
    apellidos = models.CharField(max_length = 220, blank= False, null = False)
    nacionalidad = models.CharField(max_length = 100, blank= False, null = False)
    descripcion = models.TextField(blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now= True, auto_now_add= False)
    

    # en la clase meta le indico con verbose como escribir sus nombres en admin
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['apellidos']

        # con esta fucion puedo ver en admin el nombre de los objetos apellido autor
    def __str__(self):
        return self.apellidos
# OnToOneField = relacion de 1 en 1, on_delete= models.CASCADE
# ForeignKey   de 1 a muchos con clave foranea, on_delete= models.CASCADE
# ManyToManyField de muchos a muchos, no lleva on_delete
class Libro (models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 255, blank= False, null = False)
    fecha_publicacion = models.DateField(Autor)
    autor_id = models.ManyToManyField (Autor)
    fecha_creacion = models.DateField('Fecha de creación', auto_now= True, auto_now_add= False)


    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
