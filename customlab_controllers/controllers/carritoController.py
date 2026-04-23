from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.carritoService import CarritoService
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCarritoByUserId(request):
    user_id = request.user.id_usuario
    carrito = CarritoService.getCarritoByUserId(user_id)
    if carrito['success']:
        # Transform image paths to absolute URLs
        for item in carrito['data']:
            if item['producto'].get('imagen'):
                item['producto']['imagen'] = request.build_absolute_uri(item['producto']['imagen'])
        return Response(carrito, status=200)
    else:
        return Response(carrito, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addItemToCarrito(request):
    data = request.data
    id_usuario = request.user.id_usuario
    id_producto = data.get('id_producto')
    id_talla = data.get('id_talla')
    cantidad = data.get('cantidad')

    if not all([id_usuario, id_producto, id_talla, cantidad]):
        return Response({
            'success': False,
            'message': 'Faltan parámetros requeridos: id_usuario, id_producto, id_talla, cantidad'
        }, status=400)

    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            return Response({
                'success': False,
                'message': 'La cantidad debe ser mayor a 0'
            }, status=400)
    except ValueError:
        return Response({
            'success': False,
            'message': 'La cantidad debe ser un número entero'
        }, status=400)

    result = CarritoService.addItemToCarrito(id_usuario, id_producto, id_talla, cantidad)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCarritoItem(request):
    data = request.data
    id_usuario = request.user.id_usuario
    id_producto = data.get('id_producto')
    id_talla = data.get('id_talla')
    cantidad = data.get('cantidad')

    if not all([id_usuario, id_producto, id_talla, cantidad is not None]):
        return Response({
            'success': False,
            'message': 'Faltan parámetros requeridos: id_usuario, id_producto, id_talla, cantidad'
        }, status=400)

    try:
        cantidad = int(cantidad)
    except ValueError:
        return Response({
            'success': False,
            'message': 'La cantidad debe ser un número entero'
        }, status=400)

    result = CarritoService.updateCarritoItem(id_usuario, id_producto, id_talla, cantidad)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeItemFromCarrito(request):
    data = request.data
    id_usuario = request.user.id_usuario
    id_producto = data.get('id_producto')
    id_talla = data.get('id_talla')

    if not all([id_usuario, id_producto, id_talla]):
        return Response({
            'success': False,
            'message': 'Faltan parámetros requeridos: id_usuario, id_producto, id_talla'
        }, status=400)

    result = CarritoService.removeItemFromCarrito(id_usuario, id_producto, id_talla)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def clearCarrito(request):
    user_id = request.user.id_usuario
    result = CarritoService.clearCarrito(user_id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)