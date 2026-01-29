from django.urls import path
from .controllers.productController import getProductos, getProductoById, createProducto

urlpatterns = [
    path('productos/', getProductos),
    path('productos/<int:id>/', getProductoById),
    path('productos/create/', createProducto),
]