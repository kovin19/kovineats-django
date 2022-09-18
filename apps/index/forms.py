from django import forms
from .models import CarritoModel, PedidoModel

class PedidoForm(forms.ModelForm):

    class Meta:
        model = PedidoModel
        fields = ['total','platillos','ingredientes']

# This form is for validating the data
# in the modal
class CarritoForm(forms.ModelForm):

    class Meta:
        model = CarritoModel
        fields = ['total','platillos','ingredientes']
