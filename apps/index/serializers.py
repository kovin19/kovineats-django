from rest_framework import serializers
from .models import PedidoModel, RepartidorModel

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PedidoModel
        exclude = ['ingredientes','platillos','repartidor']

class RepartidorSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepartidorModel
        fields = '__all__'