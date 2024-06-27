from registro_conductores.models import Conductor, Direccion, Vehiculo

def crear_conductor(nombre,apellido,fecha_nac):
    c =Conductor(nombre=nombre, apellido=apellido, fecha_nac= fecha_nac)
    c.save()
    
def agregar_direccion(calle,numero,comuna,region,conductor_id):
    d= Direccion(calle=calle, numero=numero,comuna=comuna, region=region, conductor_id=conductor_id)
    d.save()
    
    imprimir_modelos()
    
def agregar_vehiculo(patente = str, marca=str, modelo=str, año=int, conductor_id= int):
    pass

def eliminar_vehiculo():
    pass

def eliminar_conductor():
    pass

def imprimir_modelos():
    conductores = Conductor.objects.all()
    direcciones = Direccion.objects.all()
    print (conductores)
    print (direcciones)