from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from customlab_services.services.usuarioService import UsuarioService
from django_ratelimit.decorators import ratelimit
from rest_framework.permissions import AllowAny, IsAuthenticated
from customlab_api.permissions import IsAdmin, IsAdminOrManager,IsCliente

@ratelimit(key='ip', rate='5/m', block=True)
@api_view(['POST'])
@permission_classes([AllowAny])
def loginUsuario(request):
    data = request.data
    result = UsuarioService.verifyUsuario(data)
    if result['success']:
        return Response(result, status=200)
    if result.get('message'):
        return Response(result, status=400)
    return Response(result, status=401)

@api_view(['GET'])
@permission_classes([IsAdminOrManager])
def getUsuarios(request):
    usuarios = UsuarioService.getUsuarios()
    if usuarios ['success']:
        return Response(usuarios, status=200)
    else:
        return Response(usuarios, status=404)

@api_view(['GET'])
@permission_classes([IsAdminOrManager])
def getUsuarioById(request, id):
    usuario = UsuarioService.getUsuarioById(id)
    if usuario ['success']:
        return Response(usuario, status=200)
    else:
        return Response(usuario, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyUsuario(request):
    id = request.user.id_usuario
    usuario = UsuarioService.getUsuarioById(id)
    if usuario ['success']:
        return Response(usuario, status=200)
    else:
        return Response(usuario, status=404)

@api_view(['POST'])
@permission_classes([IsAdminOrManager])
def createUsuario(request):
    data = request.data
    result = UsuarioService.createUsuario(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)

@api_view(['PATCH'])
@permission_classes([IsAdminOrManager])
def updateUsuario(request, id):
    if request.user.id_usuario != id and request.user.rol != 'admin':
        return Response({
            'success': False,
            'message': 'No tienes permiso para actualizar este perfil'
        }, status=403)

    data = request.data.copy()
    if request.user.rol != 'admin' and 'rol' in data:
        data.pop('rol')
    
    if 'password' in data:
        data.pop('password')

    result = UsuarioService.updateUsuario(id, data)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['PATCH'])
@permission_classes([IsAdminOrManager])
def updatePassword(request, id):
    if request.user.id_usuario != id and request.user.rol != 'admin':
        return Response({
            'success': False,
            'message': 'No tienes permiso para actualizar esta contraseña'
        }, status=403)

    data = request.data
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    if not old_password or not new_password:
        return Response({
            'success': False,
            'message': 'Se requieren old_password y new_password'
        }, status=400)

    result = UsuarioService.updatePassword(id, old_password, new_password)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['DELETE'])
@permission_classes([IsAdminOrManager])
def deleteUsuario(request, id):
    if request.user.id_usuario != id and request.user.rol != 'admin':
        return Response({
            'success': False,
            'message': 'No tienes permiso para eliminar este perfil'
        }, status=403)

    result = UsuarioService.deleteUsuario(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)