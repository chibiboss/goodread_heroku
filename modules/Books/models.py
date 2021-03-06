from django.db import models
from modules.Authors.models import Author
from django.conf import settings

# Create your models here.

class Book(models.Model):
    GENEROS = (
        ("DR","Drama"),
        ("CM","Comedia"),
        ("FT","Fantasia"),
        ("CF","Ciencia Ficción"),
        ("PS","Poesia"),
        ("LC","Literatura Contemporanea"),
        ("LH","Literatura Hispana"),
        ("LU","Literatura Universal"),
        ("HS","Historica")
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    autor  = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="libros")
    ISBN = models.CharField(max_length=100,unique=True)
    fecha_publicacio = models.DateField(null=True)
    foto_portada = models.URLField(blank=True, null=True)
    descripcion = models.TextField()
    rating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00)
    genero_literario = models.CharField(choices=GENEROS,max_length=100)

    def __str__(self):
        return "Libro: %s " % (self.nombre)

class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="comentarios")
    commentario = models.TextField()