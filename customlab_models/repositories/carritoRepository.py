from customlab_models.models import Carrito


class CarritoRepository:
    @staticmethod
    def getCarritoByUserId(id_usuario):
        carrito = Carrito.objects.filter(id_usuario_id=id_usuario).values(
            'id_usuario', 'id_producto', 'cantidad', 'precio_total'
        ).order_by('id_producto')
        if not carrito.exists():
            return False
        return list(carrito)

    @staticmethod
    def getCarritoItem(id_usuario, id_producto):
        carrito_item = Carrito.objects.filter(
            id_usuario_id=id_usuario,
            id_producto_id=id_producto
        ).values('id_usuario', 'id_producto', 'cantidad', 'precio_total').first()
        return carrito_item or None

    @staticmethod
    def createCarritoItem(id_usuario, id_producto, cantidad, precio_total):
        try:
            Carrito.objects.create(
                id_usuario_id=id_usuario,
                id_producto_id=id_producto,
                cantidad=cantidad,
                precio_total=precio_total
            )
            return True
        except Exception:
            return False

    @staticmethod
    def updateCarritoItem(id_usuario, id_producto, cantidad, precio_total):
        updated = Carrito.objects.filter(
            id_usuario_id=id_usuario,
            id_producto_id=id_producto
        ).update(
            cantidad=cantidad,
            precio_total=precio_total
        )
        return updated > 0

    @staticmethod
    def deleteCarritoItem(id_usuario, id_producto):
        deleted, _ = Carrito.objects.filter(
            id_usuario_id=id_usuario,
            id_producto_id=id_producto
        ).delete()
        return deleted > 0

    @staticmethod
    def clearCarritoByUserId(id_usuario):
        deleted, _ = Carrito.objects.filter(id_usuario_id=id_usuario).delete()
        return deleted >= 0
