from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.usuarioService import UsuarioService

@api_view(['GET'])
def getUsuarios(request):
    usuarios = UsuarioService.getUsuarios()
    if usuarios is None:
        return Response({'error': 'No users found'}, status=404)
    return Response(usuarios)

@api_view(['GET'])
def getUsuarioById(request, id):
    usuario = UsuarioService.getUsuarioById(id)
    if usuario is None:
        return Response({'error': 'Usuario not found'}, status=404)
    return Response(usuario)

@api_view(['POST'])
def createUsuario(request):
    data = request.data
    new_user = UsuarioService.createUsuario(data)
    return Response(new_user, status=201)

@api_view(['PUT'])
def updateUsuario(request, id):
    data = request.data
    updated_user = UsuarioService.updateUsuario(id, data)
    if updated_user is None:
        return Response({'error': 'Usuario not found'}, status=404)
    return Response(updated_user)

@api_view(['DELETE'])
def deleteUsuario(request, id):
    success = UsuarioService.deleteUsuario(id)
    if not success:
        return Response({'error': 'Usuario not found'}, status=404)
    return Response(status=204)