from django.db import models

# Create your models here.

# All this classes are used to define the database
# models needed for this project
class IngredienteModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'ingredientes'

class RestauranteModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10)
    horario = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'restaurantes'

class PlatilloModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)
    restaurante = models.ForeignKey('RestauranteModel', on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(IngredienteModel)

    class Meta:
        db_table = 'platillos'

class RepartidorModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    acepta_pedidos = models.BooleanField(default=True)

    class Meta:
        db_table = 'repartidor'
        ordering = ['-id']

class PedidoModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    folio = models.CharField(max_length=255)
    total = models.CharField(max_length=255)
    repartidor = models.CharField(max_length=255)
    fecha_pedido = models.DateTimeField(auto_now=True)
    ingredientes = models.ManyToManyField(IngredienteModel)
    platillos = models.ManyToManyField(PlatilloModel)
    activo = models.BooleanField(default=True)
    repartidor_id = models.ForeignKey(RepartidorModel, on_delete=models.CASCADE, related_name='repartidor', null=True, blank=True)
    tiempo_entrega = models.CharField(max_length=255,null=True, blank=True)
    hora_entrega = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'pedidos'
        ordering = ['-id']

class CarritoModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    platillos = models.ManyToManyField(PlatilloModel)
    ingredientes = models.ManyToManyField(IngredienteModel)
    # user
    total = models.FloatField()

    class Meta:
        db_table = 'carrito'
        ordering = ['id']
