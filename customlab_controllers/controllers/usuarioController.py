from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.usuarioService import UsuarioService

@api_view(['GET'])
def getUsuarios(request):
    usuarios = UsuarioService.getUsuarios()
    if usuarios ['success']:
        return Response(usuarios, status=200)
    else:
        return Response(usuarios, status=404)

@api_view(['GET'])
def getUsuarioById(request, id):
    usuario = UsuarioService.getUsuarioById(id)
    if usuario ['success']:
        return Response(usuario, status=200)
    else:
        return Response(usuario, status=404)

@api_view(['POST'])
def createUsuario(request):
    data = request.data
    result = UsuarioService.createUsuario(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)

@api_view(['POST'])
def loginUsuario(request):
    data = request.data
    result = UsuarioService.verifyUsuario(data)
    if result['success']:
        return Response(result, status=200)
    if result.get('message') == 'Email y password son obligatorios':
        return Response(result, status=400)
    return Response(result, status=401)

@api_view(['PUT'])
def updateUsuario(request, id):
    data = request.data
    result = UsuarioService.updateUsuario(id, data)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['DELETE'])
def deleteUsuario(request, id):
    result = UsuarioService.deleteUsuario(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)