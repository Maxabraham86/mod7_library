from django.core.management.base import BaseCommand
from registro_conductores.services import *


class Command(BaseCommand):

    def handle (self, *args, **kwargs):
    
        crear_conductor('Pedro', 'Picapiedra', '1960-09-15')
        
        agregar_direccion('Av. Rocadura', '1234', 'Piedradura', 'v',3)
        # c.save()
        print ( 'agregar conductor')