from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.usuarioService import UsuarioService

@api_view(['GET'])
def getProductos(request):
    usuarios = UsuarioService.getProductos()
    if usuarios is None:
        return Response({'error': 'No products found'}, status=404)
    return Response(usuarios)

@api_view(['GET'])
def getProductoById(request, id):
    usuario = UsuarioService.getProductoById(id)
    if usuario is None:
        return Response({'error': 'Producto not found'}, status=404)
    return Response(usuario)

@api_view(['POST'])
def createProducto(request):
    data = request.data
    new_user = UsuarioService.createProducto(data)
    return Response(new_user, status=201)

@api_view(['PUT'])
def updateProducto(request, id):
    data = request.data
    updated_user = UsuarioService.updateProducto(id, data)
    if updated_user is None:
        return Response({'error': 'Producto not found'}, status=404)
    return Response(updated_user)

@api_view(['DELETE'])
def deleteProducto(request, id):
    success = UsuarioService.deleteProducto(id)
    if not success:
        return Response({'error': 'Producto not found'}, status=404)
    return Response(status=204)