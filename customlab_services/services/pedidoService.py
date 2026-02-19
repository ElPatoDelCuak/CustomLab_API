from customlab_models.repositories.pedidoRepository import PedidoRepository

class PedidoService:
    @staticmethod
    def getPedidos():
        pedidos = PedidoRepository.getPedidos()
        if pedidos:
            return {
                'success': True,
                'data': list(pedidos)
            }
        return {
            'success': False,
            'message': 'No orders found'
        }

    @staticmethod
    def getPedidoById(idPedido):
        pedido = PedidoRepository.getPedidoById(idPedido)
        if pedido:
            return {
                'success': True,
                'data': pedido
            }
        return {
            'success': False,
            'message': 'Pedido not found'
        }

    @staticmethod
    def createPedido(data):
        exist = PedidoRepository.getPedidoById(data.get('id_pedido'))
        if exist:
            return {
                'success': False,
                'message': 'El pedido ya existe'
            }
        success = PedidoRepository.createPedido(data)
        if success:
            return {
                'success': True,
                'message': 'Pedido creado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al crear el pedido'
        }
    
    @staticmethod
    def updatePedido(idPedido, data):
        exist = PedidoRepository.getPedidoById(idPedido)
        if not exist:
            return {
                'success': False,
                'message': 'Pedido no encontrado'
            }
        success = PedidoRepository.updatePedido(idPedido, data)
        if success:
            return {
                'success': True,
                'message': 'Pedido actualizado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al actualizar el pedido'
        }
    
    @staticmethod
    def deletePedido(idPedido):
        exist = PedidoRepository.getPedidoById(idPedido)
        if not exist:
            return {
                'success': False,
                'message': 'Pedido no encontrado'
            }
        success = PedidoRepository.deletePedido(idPedido)
        if success:
            return {
                'success': True,
                'message': 'Pedido eliminado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al eliminar el pedido'
        }
    @staticmethod
    def verifyPedido(data):
        pass
    @staticmethod
    def verifyUpdatePedido(data):
        pass
    def calcularTotalPedido(idPedido):
        pass
    def cambiarEstadoPedido(idPedido, estado):
        pass
