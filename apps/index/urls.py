from django.urls import path
from .views import IndexView, CreatePedido, ShowPedidos, AddToCart

app_name = 'index'

# These are the urls used in the project
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('crearPedido/', CreatePedido.as_view(), name='create'),
    path('verPedidos/', ShowPedidos.as_view(), name='show'),
    path('agregarCarrito/', AddToCart.as_view(), name='add')
]
