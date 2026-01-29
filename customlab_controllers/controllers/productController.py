from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.productoService import ProductoService

@api_view(['GET'])
def getProductos(request):
    productos = ProductoService.getProductos()
    if productos is None:
        return Response({'error': 'No products found'}, status=404)
    return Response(productos)

@api_view(['GET'])
def getProductoById(request, id):
    producto = ProductoService.getProductoById(id)
    if producto is None:
        return Response({'error': 'Producto not found'}, status=404)
    return Response(producto)

@api_view(['POST'])
def createProducto(request):
    data = request.data
    new_product = ProductoService.createProducto(data)
    return Response(new_product, status=201)