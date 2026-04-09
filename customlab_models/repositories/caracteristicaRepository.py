from customlab_models.models import Caracteristicas
from customlab_models.models import CaracteristicaProducto

class CaracteristicaRepository:
    @staticmethod
    def getCaracteristicas():
        caracteristicas = Caracteristicas.objects.all().order_by('id_caracteristica').values(
            'id_caracteristica', 'caracteristica'
        )
        if not caracteristicas.exists():
            return False
        return list(caracteristicas)
    
    @staticmethod
    def getCaracteristicaById(id):
        caracteristica = Caracteristicas.objects.filter(id_caracteristica=id).values(
            'id_caracteristica', 'caracteristica'
        ).first()
        if not caracteristica:
            return False
        return caracteristica
    
    @staticmethod
    def createCaracteristica(data):
        Caracteristicas.objects.create(
            caracteristica=data.get('caracteristica')
        )
        if Caracteristicas.objects.exists():
            return True
        return False
    
    @staticmethod
    def deleteCaracteristica(id):
        Caracteristicas.objects.filter(id_caracteristica=id).delete()
        if not Caracteristicas.objects.filter(id_caracteristica=id).exists():
            return True
        return False
    
    @staticmethod
    def addCaracteristicaToProducto(id_producto, id_caracteristica):
        CaracteristicaProducto.objects.create(
            id_producto_id=id_producto,
            id_caracteristica_id=id_caracteristica
        )
        if CaracteristicaProducto.objects.filter(id_producto_id=id_producto, id_caracteristica_id=id_caracteristica).exists():
            return True
        return False