from customlab_models.models import Tallas
class TallaRepository:
    @staticmethod
    def getTallas():
        tallas = Tallas.objects.all().values(
            'id_talla','id_producto','talla','stock'
        )
        if not tallas.exists():
            return False
        return tallas

    @staticmethod
    def getTallaById(idTalla):
        talla = Tallas.objects.filter(id_talla=idTalla).values(
            'id_talla','id_producto','talla','stock'
        ).first()
        if not talla.exists():
            return False
        return talla
    
    @staticmethod
    def getTallasByProductoId(idProducto):
        tallas = Tallas.objects.filter(id_producto=idProducto).values(
            'id_talla','id_producto','talla','stock'
        )
        if not tallas.exists():
            return False
        return tallas

    @staticmethod
    def getTallaById(idTalla):
        talla = Tallas.objects.filter(id_talla=idTalla).values(
            'id_talla','id_producto','talla','stock'
        ).first()
        return talla or None

    @staticmethod
    def createTalla(data):
        Tallas.objects.create(
            id_producto_id=data.get('id_producto'),
            talla=data.get('talla'),
            stock=data.get('stock'),
        )
        if Tallas.objects.exists():
            return True
        return False
    
    @staticmethod
    def updateTalla(idTalla, data):
        Tallas.objects.filter(id_talla=idTalla).update(
            id_producto=data.get('id_producto'),
            talla=data.get('talla'),
            stock=data.get('stock'),
        )
        if Tallas.objects.filter(id_talla=idTalla).exists():
            return True
        return False
    
    @staticmethod
    def deleteTalla(idTalla):
        Tallas.objects.filter(id_talla=idTalla).delete()
        if not Tallas.objects.filter(id_talla=idTalla).exists():
            return True
        return False
    @staticmethod
    def deleteTallasByProductoId(idProducto):
        Tallas.objects.filter(id_producto=idProducto).delete()
        return not Tallas.objects.filter(id_producto=idProducto).exists()
