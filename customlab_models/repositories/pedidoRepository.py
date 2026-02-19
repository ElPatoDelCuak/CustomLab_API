from customlab_models.models import Pedidos
from customlab_models.models import Usuarios

class PedidoRepository:
    @staticmethod
    def getPedidos():
        pedidos = Pedidos.objects.all().order_by('id_pedido').values(
            'id_pedido', 'id_usuario', 'estado', 'total',
            'fecha', 'direccion', 'numero_piso'
        )
        if not pedidos.exists():
            return False
        return pedidos

    @staticmethod
    def getPedidoById(idPedido):
        pedido =  Pedidos.objects.filter(id_pedido=idPedido).values(
            'id_pedido', 'id_usuario', 'estado', 'total',
            'fecha', 'direccion', 'numero_piso'
        )
        if not pedido.exists():
            return False
        return pedido

    @staticmethod
    def createPedido(data):
        Pedidos.objects.create(
            id_usuario=data.get('id_usuario'),
            estado=data.get('estado'),
            total=data.get('total'),
            direccion=data.get('direccion'),
            numero_piso=data.get('numero_piso'),
        )
        if Pedidos.objects.exists():
            return True
        return False

    @staticmethod
    def updatePedido(idPedido, data):
        Pedidos.objects.filter(id_pedido=idPedido).update(
            id_usuario=data.get('id_usuario'),
            estado=data.get('estado'),
            total=data.get('total'),
            direccion=data.get('direccion'),
            numero_piso=data.get('numero_piso'),
        )
        if Pedidos.objects.filter(id_pedido=idPedido).exists():
            return True
        return False

    @staticmethod
    def deletePedido(idPedido):
        Pedidos.objects.filter(id_pedido=idPedido).delete()
        if not Pedidos.objects.filter(id_pedido=idPedido).exists():
            return True
        return False
    @staticmethod
    def updateEstadoPedido(idPedido, estado):
        pass