from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Client (models.Model):
    first_name= models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email=models.EmailField(unique=True)
    height = models.DecimalField(decimal_places=2, max_digits=3)
    active = models.BooleanField(default=True) 
    #marcas temporales
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
class Author(models.Model):
    first_name= models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    #con ManyToMany se crea una columna fantasma en este caso 'books'
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    #year = models.IntegerField()
    year = models.IntegerField(validators= [MinValueValidator (-5000 )])
    authors= models.ManyToManyField(Author, related_name='books', through ='BookAuthors')

# Si quiero agregar informacion extra (ademas de las llaves foráneas) a la tabla intermedia,
#la creamos de la siguiente forma

class BookAuthors(models.Model):
    book= models.ForeignKey(Book, on_delete=models.CASCADE)
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    
    # agregamos extra a la tabla intermedia
    is_main = models.BooleanField(default=True)
    profit = models.IntegerField()