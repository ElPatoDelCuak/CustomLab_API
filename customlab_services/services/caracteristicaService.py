from customlab_models.repositories.caracteristicaRepository import CaracteristicaRepository
from customlab_services.services.productoService import ProductoService

class CaracteristicaService:
    @staticmethod
    def getCaracteristicas():
        caracteristicas = CaracteristicaRepository.getCaracteristicas()
        if caracteristicas:
            return {
                'success': True,
                'data': caracteristicas
            }
        return {
            'success': False,
            'message': 'No se encontraron características'
        }
    
    def getCaracteristicaById(id):
        caracteristica = CaracteristicaRepository.getCaracteristicaById(id)
        if caracteristica:
            return {
                'success': True,
                'data': caracteristica
            }
        return {
            'success': False,
            'message': 'Característica no encontrada'
        }
    
    @staticmethod
    def createCaracteristica(data):
        if not data.get('caracteristica'):
            return {
                'success': False,
                'message': 'La característica es obligatoria'
            }
        success = CaracteristicaRepository.createCaracteristica(data)
        if success:
            return {
                'success': True,
                'message': 'Característica creada exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al crear la característica'
        }
    
    @staticmethod
    def deleteCaracteristica(id):
        exist = CaracteristicaRepository.getCaracteristicaById(id)
        if not exist:
            return {
                'success': False,
                'message': 'Característica no encontrada'
            }
        success = CaracteristicaRepository.deleteCaracteristica(id)
        if success:
            return {
                'success': True,
                'message': 'Característica eliminada exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al eliminar la característica'
        }
    
    @staticmethod
    def addCaracteristicaToProducto(id_producto, id_caracteristica):
        try:
            id_producto = int(id_producto)
            id_caracteristica = int(id_caracteristica)
        except ValueError:
            return {
                'success': False,
                'message': 'id_producto e id_caracteristica deben ser enteros'
            }
        existCaracteristica = CaracteristicaService.getCaracteristicaById(id_caracteristica)
        if not existCaracteristica['success']:
            return {
                'success': False,
                'message': 'Característica no encontrada'
            }
        existProducto = ProductoService.getProductoById(id_producto)
        if not existProducto['success']:
            return {
                'success': False,
                'message': 'Producto no encontrado'
            }
        success = CaracteristicaRepository.addCaracteristicaToProducto(id_producto, id_caracteristica)
        if not success:
            return {
                'success': False,
                'message': 'Error al agregar la característica al producto'
            }
        return {
            'success': True,
            'message': 'Característica agregada al producto exitosamente'
        }
    
    #! EL RAUL ES UN BOBO MESOPOTAMICO, NO TOCARLO, PELIGRO DE SIDA

    @staticmethod
    def removeCaracteristicaFromProducto(id_producto, id_caracteristica):
        try:
            id_producto = int(id_producto)
            id_caracteristica = int(id_caracteristica)
        except ValueError:
            return {
                'success': False,
                'message': 'id_producto e id_caracteristica deben ser enteros'
            }
        existCaracteristica = CaracteristicaService.getCaracteristicaById(id_caracteristica)
        if not existCaracteristica['success']:
            return {
                'success': False,
                'message': 'Característica no encontrada'
            }
        existProducto = ProductoService.getProductoById(id_producto)
        if not existProducto['success']:
            return {
                'success': False,
                'message': 'Producto no encontrado'
            }
        success = CaracteristicaRepository.removeCaracteristicaFromProducto(id_producto, id_caracteristica)
        if not success:
            return {
                'success': False,
                'message': 'Error al eliminar la característica del producto'
            }
        return {
            'success': True,
            'message': 'Característica eliminada del producto exitosamente'
        }