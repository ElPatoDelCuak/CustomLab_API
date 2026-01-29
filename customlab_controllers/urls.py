from django.urls import path
from .controllers.productController import getProductos, getProductoById, createProducto, updateProducto, deleteProducto

urlpatterns = [
    path('productos/', getProductos),
    path('productos/<int:id>/', getProductoById),
    path('productos/create/', createProducto),
    path('productos/update/<int:id>/', updateProducto),
    path('productos/delete/<int:id>/', deleteProducto),
]