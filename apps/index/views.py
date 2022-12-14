from ast import Delete
from django.db.models import Q
from datetime import datetime,timezone
from random import random
from django.shortcuts import redirect
from django.views.generic import ListView, View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
import json, pytz

from apps.index.forms import CarritoForm, PedidoForm
from .models import CarritoModel, IngredienteModel, PedidoModel, RestauranteModel, PlatilloModel, RepartidorModel
from .serializers import PedidoSerializer, RepartidorSerializer

# Create your views here.

contFolio = 1

# This loads the information in the index
class IndexView(ListView):
    model = RestauranteModel
    template_name = 'index.html'

    # With these method we call al the information from the database
    # and put it on the front
    def get_context_data(self, **kwargs):
        context = {}
        context['platillos'] = PlatilloModel.objects.all()
        context['restaurantes'] = RestauranteModel.objects.all()
        context['ingredientes'] = IngredienteModel.objects.all()
        context['carrito'] = CarritoModel.objects.all()
        context['productosCarrito'] = CarritoModel.objects.all().count()
        return context

# This method is for creating a pedido
class CreatePedido(View):
    success_url = 'index:index'

    # This method generates a folio
    def generate_folio(self, id):
        dia = datetime.today().strftime('%Y%m%d')
        return 'KOVINEATS' + dia + '000' + str(int(random()*300)) + str(id)

    # This methpd generates a random repartidor using arrays with names and lastnames
    def generate_repartidor(self):
        nombres = ['Marcos','Diego','Juan','Gonzalo','Paul']
        apellidos = ['Quiles','Valles','Baena','Herrera','Zamorano','Espinoza','Sevillano','Ballesteros','Matos','Vasquez']
        nombre = nombres[int(random()*5)] + ' ' + apellidos[int(random()*10)] + ' ' + apellidos[int(random()*10)]
        return nombre

    # This method is for the request
    def post(self, request):
        ingredientes = request.POST.getlist('ingredientes')
        platillos = request.POST.getlist('platillos')
        # for platillo in platillos:
        #     for ingrediente in ingredientes:
        #         ingrediente = IngredienteModel.objects.filter(platillomodel=platillo,id=ingrediente)
        #         if(ingrediente):
        #             print(ingrediente)
        total = request.POST.getlist('total')
        
        fecha_pedido = datetime.now()
        repartidor = self.generate_repartidor()

        pedido = PedidoModel.objects.create(total=total[0], repartidor = '')

        # In this method we go through the platillos in the carrito
        # we get the platillo object and filter the ingredientes, adding them to
        # the pedido
        for id in platillos:
            platillo = PlatilloModel.objects.get(id=id)
            for ingrediente in ingredientes:
                ingredientes_list = IngredienteModel.objects.filter(
                    Q(id=ingrediente) & Q(platillomodel=platillo)
                )
                if(ingredientes_list):
                    pedido.ingredientes.add(ingredientes_list.get(pk=ingrediente))
            pedido.platillos.add(platillo)

        pedido.folio = self.generate_folio(pedido.id)
        pedido.save()
        CarritoModel.objects.all().delete()
        mensaje = messages.info(request, 'Pedido realizado. El restaurante preparar?? la orden.')


        # This method was for ordering just one platillo at the time
        # form = PedidoForm(request.POST)

        # if form.is_valid():
        #     pedido = form.save()
        #     pedido.fecha_pedido = datetime.today().strftime('%Y-%m-%d')
        #     pedido.folio = self.generate_folio(pedido.id)
        #     pedido.repartidor = self.generate_repartidor()
        #     platillo = PlatilloModel.objects.get(pk=platillo_id)
        #     pedido.platillos.add(platillo)

        #     for ingrediente in ingredientes:
        #         pedido.ingredientes.add(IngredienteModel.objects.get(id=ingrediente))
            
        #     pedido.save()
        return HttpResponseRedirect(reverse_lazy('index:index'))

# This method is for deploying the information in the fron of pedidos
class ShowPedidos(ListView):
    model = PedidoModel
    template_name = 'pedidos.html'
    context_object_name = 'pedidos'

    def get_context_data(self, **kwargs):
        context = {}
        context['pedidos'] = PedidoModel.objects.all()
        context['ingredientes'] = IngredienteModel.objects.all()
        context['platillos'] = IngredienteModel.objects.all()
        return context

# This method is used to add products to the carrito
class AddToCart(APIView):
    
    def post(self, request):
        carrito_form = CarritoForm(request.POST)
        if carrito_form.is_valid():
            carrito_form.save() 
            messages.success(request, 'El platillo se ha agregado al carrito.')
        return HttpResponseRedirect(reverse_lazy('index:index'))

class AsignarPedido(APIView):

    # def get(self, request):
    #     print(request.POST)
    #     return Response({"message":"hola"})

    def post(self, request):
        repartidor = RepartidorModel.objects.filter(acepta_pedidos=True).first()
        pedido = PedidoModel.objects.filter(activo=True).first()
        pedido_serializer = PedidoSerializer(data=pedido.__dict__, instance=pedido)
        if pedido_serializer.is_valid():
            pedido_instance = pedido_serializer.save(activo=False, repartidor_id=repartidor)
            repartidor.acepta_pedidos = False
            repartidor.save()
            return Response(pedido_serializer.data)
        return Response({"Message":"Not found"})

class EntregarPedido(APIView):

    def post(self, request):
        pedido_id = request.data['id']
        pedido = PedidoModel.objects.get(id=pedido_id)
        print(pedido.fecha_pedido.replace(tzinfo=None))
        fecha_pedido = pedido.fecha_pedido
        difference = datetime.utcnow().replace(tzinfo=pytz.UTC) - fecha_pedido.replace(tzinfo=pytz.UTC)
        pedido.hora_entrega = datetime.now()
        pedido.tiempo_entrega = difference
        pedido.activo = False
        pedido.save()
        return Response(200)

class PedidoEntregado(ListView):
    model = PedidoModel
    template_name = 'pedidos_entregados.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        queryset = PedidoModel.objects.filter(Q(tiempo_entrega__isnull=False))
        print(queryset)
        return queryset