from django.db import models

# Create your models here.

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

class PedidoModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    folio = models.CharField(max_length=255)
    total = models.CharField(max_length=255)
    repartidor = models.CharField(max_length=255)
    fecha_pedido = models.DateField(blank=True, null=True)
    ingredientes = models.ManyToManyField(IngredienteModel)
    platillos = models.ManyToManyField(PlatilloModel)

    class Meta:
        db_table = 'pedidos'

class CarritoModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    platillos = models.ManyToManyField(PlatilloModel)
    ingredientes = models.ManyToManyField(IngredienteModel)
    # user
    total = models.FloatField()

    class Meta:
        db_table = 'carrito'
        ordering = ['id']