from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.productoService import ProductoService

@api_view(['GET'])
def getProductos(request):
    productos = ProductoService.getProductos()
    if productos['success']:
        return Response(productos, status=200)
    else:
        return Response(productos, status=404)

@api_view(['GET'])
def getProductoById(request, id):
    producto = ProductoService.getProductoById(id)
    if producto['success']:
        return Response(producto, status=200)
    else:
        return Response(producto, status=404)

@api_view(['POST'])
def createProducto(request):
    data = request.data
    images = request.FILES.getlist('images')
    result = ProductoService.createProducto(data, images)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)

@api_view(['PUT'])
def updateProducto(request, id):
    data = request.data
    result = ProductoService.updateProducto(id, data)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['DELETE'])
def deleteProducto(request, id):
    result = ProductoService.deleteProducto(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)