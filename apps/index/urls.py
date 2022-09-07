from django.urls import path
from .views import IndexView, CreatePedido, ShowPedidos

app_name = 'index'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('createPedido/', CreatePedido.as_view(), name='create'),
    path('verPedidos/', ShowPedidos.as_view(), name='show')
]