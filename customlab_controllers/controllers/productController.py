from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.productoService import ProductoService

@api_view(['GET'])
def getProductos(request):
    productos = ProductoService.getProductos()
    return Response(productos)

@api_view(['GET'])
def getProductoById(request, id):
    producto = ProductoService.getProductoById(id)
    if not producto:
        return Response({"message": "Producto no encontrado"}, status=404)
    return Response(producto)
