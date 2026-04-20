from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.carritoService import CarritoService


@api_view(['GET'])
def getCarritoByUserId(request, user_id):
    carrito = CarritoService.getCarritoByUserId(user_id)
    if carrito['success']:
        return Response(carrito, status=200)
    else:
        return Response(carrito, status=404)


@api_view(['POST'])
def addItemToCarrito(request):
    data = request.data
    id_usuario = data.get('id_usuario')
    id_producto = data.get('id_producto')
    cantidad = data.get('cantidad')

    if not all([id_usuario, id_producto, cantidad]):
        return Response({
            'success': False,
            'message': 'Faltan parámetros requeridos: id_usuario, id_producto, cantidad'
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

    result = CarritoService.addItemToCarrito(id_usuario, id_producto, cantidad)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)


@api_view(['PUT'])
def updateCarritoItem(request):
    data = request.data
    id_usuario = data.get('id_usuario')
    id_producto = data.get('id_producto')
    cantidad = data.get('cantidad')

    if not all([id_usuario, id_producto, cantidad is not None]):
        return Response({
            'success': False,
            'message': 'Faltan parámetros requeridos: id_usuario, id_producto, cantidad'
        }, status=400)

    try:
        cantidad = int(cantidad)
    except ValueError:
        return Response({
            'success': False,
            'message': 'La cantidad debe ser un número entero'
        }, status=400)

    result = CarritoService.updateCarritoItem(id_usuario, id_producto, cantidad)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)


@api_view(['DELETE'])
def removeItemFromCarrito(request):
    data = request.data
    id_usuario = data.get('id_usuario')
    id_producto = data.get('id_producto')

    if not all([id_usuario, id_producto]):
        return Response({
            'success': False,
            'message': 'Faltan parámetros requeridos: id_usuario, id_producto'
        }, status=400)

    result = CarritoService.removeItemFromCarrito(id_usuario, id_producto)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)


@api_view(['DELETE'])
def clearCarrito(request, user_id):
    result = CarritoService.clearCarrito(user_id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)