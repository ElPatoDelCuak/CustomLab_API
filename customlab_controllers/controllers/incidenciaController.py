from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.incidenciaService import IncidenciaService

@api_view(['GET'])
def getIncidencias(request):
    incidencias = IncidenciaService.getIncidencias()
    if incidencias['success']:
        return Response(incidencias, status=200)
    else:
        return Response(incidencias, status=404)
    
@api_view(['GET'])
def getIncidenciaById(request, id):
    incidencia = IncidenciaService.getIncidenciaById(id)
    if incidencia['success']:
        return Response(incidencia, status=200)
    else:
        return Response(incidencia, status=404)
    
@api_view(['POST'])
def createIncidencia(request):
    data = request.data
    result = IncidenciaService.createIncidencia(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)
    
@api_view(['PUT'])
def updateEstadoIncidencia(request, id):
    data = request.data
    result = IncidenciaService.updateEstadoIncidencia(id, data)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)
    
@api_view(['DELETE'])
def deleteIncidencia(request, id):
    result = IncidenciaService.deleteIncidencia(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)