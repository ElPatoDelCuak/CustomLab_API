from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.productoPersonalizadoService import ProductoPersonalizadoService

@api_view(['GET'])
def getProductosPersonalizados(request):
    productos = ProductoPersonalizadoService.getProductosPersonalizados()
    if productos['success']:
        return Response(productos, status=200)
    else:
        return Response(productos, status=404)

@api_view(['GET'])
def getProductoPersonalizadoById(request, id):
    producto = ProductoPersonalizadoService.getProductoPersonalizadoById(id)
    if producto['success']:
        return Response(producto, status=200)
    else:
        return Response(producto, status=404)

@api_view(['POST'])
def createProductoPersonalizado(request):
    data = request.data
    result = ProductoPersonalizadoService.createProductoPersonalizado(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)

@api_view(['PUT'])
def updateProductoPersonalizado(request, id):
    data = request.data
    result = ProductoPersonalizadoService.updateProductoPersonalizado(id, data)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['DELETE'])
def deleteProductoPersonalizado(request, id):
    result = ProductoPersonalizadoService.deleteProductoPersonalizado(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)