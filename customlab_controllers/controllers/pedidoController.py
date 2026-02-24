from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.pedidoService import PedidoService

@api_view(['GET'])
def getPedidos(request):
    pedidos = PedidoService.getPedidos()
    if pedidos['success']:
        return Response(pedidos, status=200)
    else:
        return Response(pedidos, status=404)

@api_view(['GET'])
def getPedidoById(request, id):
    pedido = PedidoService.getPedidoById(id)
    if pedido['success']:
        return Response(pedido, status=200)
    else:
        return Response(pedido, status=404)

@api_view(['POST'])
def createPedido(request):
    data = request.data
    result = PedidoService.createPedido(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)

@api_view(['PUT'])
def updatePedido(request, id):
    data = request.data
    result = PedidoService.updatePedido(id, data)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['DELETE'])
def deletePedido(request, id):
    result = PedidoService.deletePedido(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)