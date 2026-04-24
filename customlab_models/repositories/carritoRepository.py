from customlab_models.models import Carrito
from django.db.models import F


class CarritoRepository:
    @staticmethod
    def getCarritoByUserId(id_usuario):
        carrito = Carrito.objects.filter(id_usuario_id=id_usuario).values(
            'id_usuario', 'id_producto', 'id_talla', 'cantidad', 'precio_total'
        ).order_by('id_producto')
        if not carrito.exists():
            return False
        return list(carrito)

    @staticmethod
    def getCarritoItem(id_usuario, id_producto, id_talla):
        carrito_item = Carrito.objects.filter(
            id_usuario_id=id_usuario,
            id_producto_id=id_producto,
            id_talla_id=id_talla
        ).values('id_usuario', 'id_producto', 'id_talla', 'cantidad', 'precio_total').first()
        return carrito_item or None

    @staticmethod
    def createCarritoItem(id_usuario, id_producto, id_talla, cantidad, precio_total):
        try:
            Carrito.objects.create(
                id_usuario_id=id_usuario,
                id_producto_id=id_producto,
                id_talla_id=id_talla,
                cantidad=cantidad,
                precio_total=precio_total
            )
            return True
        except Exception:
            return False

    @staticmethod
    def incrementarCantidad(id_usuario, id_producto, id_talla, cantidad_a_sumar, precio_unitario):
        try:
            filas_actualizadas = Carrito.objects.filter(
                id_usuario_id=id_usuario,
                id_producto_id=id_producto,
                id_talla_id=id_talla
            ).update(
                cantidad=F('cantidad') + cantidad_a_sumar,
                precio_total=F('precio_total') + (precio_unitario * cantidad_a_sumar)
            )
            return filas_actualizadas > 0
        except Exception:
            return False
            
    @staticmethod
    def updateCarritoItem(id_usuario, id_producto, id_talla, cantidad, precio_total):
        updated = Carrito.objects.filter(
            id_usuario_id=id_usuario,
            id_producto_id=id_producto,
            id_talla_id=id_talla
        ).update(
            cantidad=cantidad,
            precio_total=precio_total
        )
        return updated > 0

    @staticmethod
    def deleteCarritoItem(id_usuario, id_producto, id_talla):
        deleted, _ = Carrito.objects.filter(
            id_usuario_id=id_usuario,
            id_producto_id=id_producto,
            id_talla_id=id_talla
        ).delete()
        return deleted > 0

    @staticmethod
    def clearCarritoByUserId(id_usuario):
        deleted, _ = Carrito.objects.filter(id_usuario_id=id_usuario).delete()
        return deleted >= 0