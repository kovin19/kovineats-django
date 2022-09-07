from django import forms
from .models import PedidoModel

class PedidoForm(forms.ModelForm):

    class Meta:
        model = PedidoModel
        fields = ['total','platillos','ingredientes']