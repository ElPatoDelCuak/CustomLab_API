from customlab_models.repositories.tallaRepository import TallaRepository

class TallaService:
    @staticmethod
    def getTallas():
        tallas = TallaRepository.getTallas()
        if not tallas:
            return {'success': False, 'message': 'No sizes found'}
        return {'success': True, 'data': list(tallas)}
    
    @staticmethod
    def getTallaById(idTalla):
        talla = TallaRepository.getTallaById(idTalla)
        if not talla:
            return {'success': False, 'message': 'Size not found'}
        return {'success': True, 'data': talla}

    @staticmethod
    def getTallasByProductoId(idProducto):
        tallas = TallaRepository.getTallasByProductoId(idProducto)
        if not tallas:
            return {'success': False, 'message': 'No sizes found for this product'}
        return {'success': True, 'data': list(tallas)}

    @staticmethod
    def createTalla(data):
        if not data.get('id_producto') or not data.get('talla') or data.get('stock') is None:
            return {'success': False, 'message': 'id_producto, talla and stock are required'}
        success = TallaRepository.createTalla(data)
        if success:
            return {'success': True, 'message': 'Size created successfully'}
        return {'success': False, 'message': 'Error creating size'}

    @staticmethod
    def updateTalla(idTalla, data):
        exist = TallaRepository.getTallaById(idTalla)
        if not exist:
            return {'success': False, 'message': 'Size not found'}
        success = TallaRepository.updateTalla(idTalla, data)
        if success:
            return {'success': True, 'message': 'Size updated successfully'}
        return {'success': False, 'message': 'Error updating size'}

    @staticmethod
    def deleteTalla(idTalla):
        exist = TallaRepository.getTallaById(idTalla)
        if not exist:
            return {'success': False, 'message': 'Size not found'}
        success = TallaRepository.deleteTalla(idTalla)
        if success:
            return {'success': True, 'message': 'Size deleted successfully'}
        return {'success': False, 'message': 'Error deleting size'}
