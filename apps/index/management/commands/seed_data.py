from ast import Delete
from django.core.management.base import BaseCommand
from apps.index.models import PlatilloModel, PedidoModel, RepartidorModel, RestauranteModel, IngredienteModel

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

def clear_data():
    PlatilloModel.objects.all().delete()
    PedidoModel.objects.all().delete()
    RestauranteModel.objects.all().delete()
    IngredienteModel.objects.all().delete()


def create_restaurantes():
    print("Creando info de restaurantes")
    restaurante = RestauranteModel(
        nombre = 'Pizzas Castillo',
        direccion = 'Calle Guatemala 523 Col. Cajeme',
        telefono = '1548789564',
        horario = '12 PM - 10 PM',
        logo_url = 'https://i.ibb.co/PFsz4BM/pizzas-castillo.png'
    )
    restaurante.save()
    restaurante = RestauranteModel(
        nombre = 'Crustaceo Cascarudo',
        direccion = 'Calle Venezuela 124 Col. Cuahutemoc',
        telefono = '2564859784',
        horario = '11 AM - 11 PM',
        logo_url = 'https://i.ibb.co/pLTypNq/crustaceo-cascarudo.png'
    )
    restaurante.save()
    restaurante = RestauranteModel(
        nombre = 'Burritos de la 69',
        direccion = 'Calle Manzanillo 478 Col. Centro',
        telefono = '1253654897',
        horario = '9 AM - 6 PM',
        logo_url = 'https://i.ibb.co/bBRjH42/burritos-69.png'
    )
    restaurante.save()
    restaurante = RestauranteModel(
        nombre = 'Sushistoso',
        direccion = 'Calle Guerrero 115 Col. America',
        telefono = '2365241025',
        horario = '11 AM - 11 PM',
        logo_url = 'https://i.ibb.co/0VpS5ZJ/sushistoso.png'
    )
    restaurante.save()
    restaurante = RestauranteModel(
        nombre = 'Tenemos de Todo',
        direccion = 'Calle Sahuaripa 1145 Col. Mexico',
        telefono = '2365258971',
        horario = '10 AM - 10 PM',
        logo_url = 'https://i.ibb.co/RHn42dW/tenemos-de-todo.png'
    )
    restaurante.save()
    print('Restaurantes creados')

def create_ingredientes():
    print('Creando ingredientes')
    ingredientes = [
        'Pepperoni', 'Jamon', 'Chorizo', 'Jalapeño', 'Cebolla', 'Tocino', 'Champiñon',
        'Lechuga','Catsup','Pepinillos','Aros de cebolla','Tomate','Mostaza','Mayonesa',
        'Queso','Salsa BBQ','Natural','Salsa Buffalo','Frijol','Papa','Chilorio','Machaca',
        'Carne Asada','Queso','Camaron','Res','Pollo','Alga'
    ]
    for ingrediente in ingredientes:
        IngredienteModel.objects.create(nombre=ingrediente)
    print('Ingredientes creados')

def create_platillos():
    print('Creando platillos')
    platillo = PlatilloModel(
        nombre = 'Pizza',
        precio = '130.00',
        descripcion = 'Pizza familiar de queso de 8 rebandas',
        logo_url = 'https://i.ibb.co/74JpfR5/pizza.png',
        restaurante = RestauranteModel.objects.get(id=1)
    )
    platillo.save()
    platillo.ingredientes.add(IngredienteModel.objects.get(id=1))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=2))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=3))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=4))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=5))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=6))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=7))
    platillo.save()
    print('Platillo 1 creado')
    platillo = PlatilloModel(
        nombre = 'Hamburguesa',
        precio = '90.00',
        descripcion = 'Hamburguesa sencilla pan y carne',
        logo_url = 'https://i.ibb.co/Nxh8yNp/hamburguesa.png',
        restaurante = RestauranteModel.objects.get(id=2)
    )
    platillo.save()
    platillo.ingredientes.add(IngredienteModel.objects.get(id=4))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=5))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=6))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=7))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=8))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=9))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=10))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=11))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=12))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=13))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=14))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=15))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=16))
    platillo.save()
    print('Platillo 2 creado')
    platillo = PlatilloModel(
        nombre = 'Boneless',
        precio = '130.00',
        descripcion = 'Orden de bonesless',
        logo_url = 'https://i.ibb.co/fkT1VSL/boneless.png',
        restaurante = RestauranteModel.objects.get(id=4)
    )
    platillo.save()
    platillo.ingredientes.add(IngredienteModel.objects.get(id=16))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=17))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=18))
    platillo.save()
    print('Platillo 3 creado')
    platillo = PlatilloModel(
        nombre = 'Burritos',
        precio = '20.00',
        descripcion = 'Excelentes burritos de harina',
        logo_url = 'https://i.ibb.co/Brn56wp/burritos.png',
        restaurante = RestauranteModel.objects.get(id=3)
    )
    platillo.save()
    platillo.ingredientes.add(IngredienteModel.objects.get(id=19))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=20))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=21))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=22))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=23))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=24))
    platillo.save()
    print('Platillo 4 creado')
    platillo = PlatilloModel(
        nombre = 'Sushi',
        precio = '130.00',
        descripcion = 'Sushis sencillos estilo california',
        logo_url = 'https://i.ibb.co/tX1G1G4/sushi.png',
        restaurante = RestauranteModel.objects.get(id=4)
    )
    platillo.save()
    platillo.ingredientes.add(IngredienteModel.objects.get(id=25))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=26))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=27))
    platillo.ingredientes.add(IngredienteModel.objects.get(id=28))
    platillo.save()
    print('Platillo 5 creado')
    platillo = PlatilloModel(
        nombre = 'Aros de cebolla',
        precio = '60.00',
        descripcion = 'Orden de aros de cebolla',
        logo_url = 'https://i.ibb.co/r7dVJrd/aros-cebolla.png',
        restaurante = RestauranteModel.objects.get(id=5)
    )
    platillo.save()
    platillo.ingredientes.add(IngredienteModel.objects.get(id=11))
    platillo.save()
    print('Platillo 6 creado')
    print('Platillos creados')

def create_repartidor():
    print('Creando repartidor')

    RepartidorModel.objects.create(
        nombre='Adrian',
        apellido_paterno='Ibarra',
        apellido_materno='Lopez',
    )

    print('Repartidor creado')

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return
    create_restaurantes()
    create_ingredientes()
    create_platillos()
    print('Se ha terminado de plantar la informacion')