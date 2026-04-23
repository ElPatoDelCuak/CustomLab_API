from customlab_models.models import Tallas
from django.db.models import Case, When, Value, IntegerField

class TallaRepository:
    SIZE_ORDER = {
        'XXS': 1, 'XS': 2, 'S': 3, 'M': 4, 'L': 5, 'XL': 6, 
        'XXL': 7, '2XL': 7, '3XL': 8, '4XL': 9, '5XL': 10
    }

    @staticmethod
    def _get_size_ordering():
        whens = [When(talla=size, then=Value(order)) for size, order in TallaRepository.SIZE_ORDER.items()]
        return Case(*whens, default=Value(99), output_field=IntegerField())

    @staticmethod
    def getTallas():
        tallas = Tallas.objects.all().annotate(
            order=TallaRepository._get_size_ordering()
        ).order_by('order').values(
            'id_talla','id_producto','talla','stock'
        )
        if not tallas.exists():
            return False
        return tallas

    @staticmethod
    def getTallasByProductoId(idProducto):
        tallas = Tallas.objects.filter(id_producto=idProducto).annotate(
            order=TallaRepository._get_size_ordering()
        ).order_by('order').values(
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
