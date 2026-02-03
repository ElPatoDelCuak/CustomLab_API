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
    result = ProductoService.createProducto(data)
    status = 201 if result['success'] else 400
    return Response(result, status=status)

@api_view(['PUT'])
def updateProducto(request, id):
    data = request.data
    result = ProductoService.updateProducto(id, data)
    status = 200 if result['success'] else 400
    return Response(result, status=status)

@api_view(['DELETE'])
def deleteProducto(request, id):
    result = ProductoService.deleteProducto(id)
    status = 200 if result['success'] else 400
    return Response(result, status=status)