from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from customlab_services.services.caracteristicaService import CaracteristicaService

@api_view(['GET'])
def getCaracteristicas(request):
    caracteristicas = CaracteristicaService.getCaracteristicas()
    if caracteristicas['success']:
        return Response(caracteristicas, status=200)
    else:
        return Response(caracteristicas, status=404)
    
@api_view(['POST'])
def createCaracteristica(request):
    data = request.data
    result = CaracteristicaService.createCaracteristica(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)
    
@api_view(['DELETE'])
def deleteCaracteristica(request, id):
    result = CaracteristicaService.deleteCaracteristica(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=404)

@api_view(['POST'])
def addCaracteristicaToProducto(request):
    data = request.data
    id_producto = data.get('id_producto')
    id_caracteristica = data.get('id_caracteristica')
    result = CaracteristicaService.addCaracteristicaToProducto(id_producto, id_caracteristica)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)