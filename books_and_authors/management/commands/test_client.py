from django.core.management.base import BaseCommand
from books_and_authors.models import Client


class Command(BaseCommand):

    def handle (self, *args, **kwargs):
    # imprimimos los argumentos opcionales del comando
    
    # probamos que se pueda agregar in nuevo Cliente
    
        c= Client(first_name='Fernando', last_name='Jara', email='fjara@gmail.com',
            height= 1.76)
    
        c.save()
        print ()