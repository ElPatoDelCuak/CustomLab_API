from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from customlab_services.services.tallaService import TallaService
from rest_framework.permissions import IsAuthenticated
from customlab_api.permissions import IsAdminOrManager

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTallas(request):
    tallas = TallaService.getTallas()
    if tallas['success']:
        return Response(tallas, status=200)
    else:
        return Response(tallas, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTallasByProductoId(request, producto_id):
    tallas = TallaService.getTallasByProductoId(producto_id)
    if tallas['success']:
        return Response(tallas, status=200)
    else:
        return Response(tallas, status=404)

@api_view(['POST'])
@permission_classes([IsAdminOrManager])
def createTalla(request):
    data = request.data
    result = TallaService.createTalla(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)

@api_view(['PUT'])
@permission_classes([IsAdminOrManager])
def updateTalla(request, id):
    data = request.data
    result = TallaService.updateTalla(id, data)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['DELETE'])
@permission_classes([IsAdminOrManager])
def deleteTalla(request, id):
    result = TallaService.deleteTalla(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)