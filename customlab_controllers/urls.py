from django.urls import path
from .controllers.productController import getProductos, getProductoById

urlpatterns = [
    path('productos/', getProductos),
    path('productos/<int:id>/', getProductoById),
]