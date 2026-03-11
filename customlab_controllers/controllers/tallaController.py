from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.tallaService import TallaService

@api_view(['GET'])
def getTallas(request):
    tallas = TallaService.getTallas()
    if tallas['success']:
        return Response(tallas, status=200)
    else:
        return Response(tallas, status=404)

@api_view(['GET'])
def getTallasByProductoId(request, producto_id):
    tallas = TallaService.getTallasByProductoId(producto_id)
    if tallas['success']:
        return Response(tallas, status=200)
    else:
        return Response(tallas, status=404)

@api_view(['POST'])
def createTalla(request):
    data = request.data
    result = TallaService.createTalla(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)

@api_view(['PUT'])
def updateTalla(request, id):
    data = request.data
    result = TallaService.updateTalla(id, data)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['DELETE'])
def deleteTalla(request, id):
    result = TallaService.deleteTalla(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)