from contextlib import redirect_stderr
from datetime import datetime
from random import seed, random
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView, View

from apps.index.forms import PedidoForm
from .models import IngredienteModel, PedidoModel, RestauranteModel, PlatilloModel

# Create your views here.

contFolio = 1

class IndexView(ListView):
    model = RestauranteModel
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['platillos'] = PlatilloModel.objects.all()
        context['restaurantes'] = RestauranteModel.objects.all()
        context['ingredientes'] = IngredienteModel.objects.all()
        return context


class CreatePedido(View):
    success_url = 'index:index'

    def generate_folio(self, id):
        dia = datetime.today().strftime('%Y%m%d')
        return 'KOVINEATS' + dia + '000' + str(int(random()*300)) + str(id)

    def generate_repartidor(self):
        nombres = ['Marcos','Diego','Juan','Gonzalo','Paul']
        apellidos = ['Quiles','Valles','Baena','Herrera','Zamorano','Espinoza','Sevillano','Ballesteros','Matos','Vasquez']
        nombre = nombres[int(random()*5)] + ' ' + apellidos[int(random()*10)] + ' ' + apellidos[int(random()*10)]
        return nombre

    def post(self, request): 
        platillo_id = request.POST.get('platillos')
        ingredientes = request.POST.getlist('ingredientes')

        form = PedidoForm(request.POST)

        if form.is_valid():
            pedido = form.save()
            pedido.fecha_pedido = datetime.today().strftime('%Y-%m-%d')
            pedido.folio = self.generate_folio(pedido.id)
            pedido.repartidor = self.generate_repartidor()
            platillo = PlatilloModel.objects.get(pk=platillo_id)
            pedido.platillos.add(platillo)

            for ingrediente in ingredientes:
                pedido.ingredientes.add(IngredienteModel.objects.get(id=ingrediente))
            
            pedido.save()
        return redirect(self.success_url)

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