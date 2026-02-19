from customlab_models.repositories.productoPersonalizadoRepository import ProductoPersonalizadoRepository

class ProductoPersonalizadoService:
    @staticmethod
    def getProductosPersonalizados():
        productos = ProductoPersonalizadoRepository.getProductosPersonalizados()
        if productos:
            return {
                'success': True,
                'data': list(productos)
            }
        return {
            'success': False,
            'message': 'No products found'
        }

    @staticmethod
    def getProductoPersonalizadoById(idProductoPersonalizado):
        producto = ProductoPersonalizadoRepository.getProductoPersonalizadoById(idProductoPersonalizado)
        if producto:
            return {
                'success': True,
                'data': producto
            }
        return {
            'success': False,
            'message': 'ProductoPersonalizado not found'
        }

    @staticmethod
    def createProductoPersonalizado(data):
        exist = ProductoPersonalizadoRepository.getProductoPersonalizadoById(data.get('id_producto'))
        if exist:
            return {
                'success': False,
                'message': 'El producto ya existe'
            }
        success = ProductoPersonalizadoRepository.createProductoPersonalizado(data)
        if success:
            return {
                'success': True,
                'message': 'ProductoPersonalizado creado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al crear el producto'
        }
    
    @staticmethod
    def updateProductoPersonalizado(idProductoPersonalizado, data):
        exist = ProductoPersonalizadoRepository.getProductoPersonalizadoById(idProductoPersonalizado)
        if not exist:
            return {
                'success': False,
                'message': 'ProductoPersonalizado no encontrado'
            }
        success = ProductoPersonalizadoRepository.updateProductoPersonalizado(idProductoPersonalizado, data)
        if success:
            return {
                'success': True,
                'message': 'ProductoPersonalizado actualizado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al actualizar el producto'
        }
    
    @staticmethod
    def deleteProductoPersonalizado(idProductoPersonalizado):
        exist = ProductoPersonalizadoRepository.getProductoPersonalizadoById(idProductoPersonalizado)
        if not exist:
            return {
                'success': False,
                'message': 'ProductoPersonalizado no encontrado'
            }
        success = ProductoPersonalizadoRepository.deleteProductoPersonalizado(idProductoPersonalizado)
        if success:
            return {
                'success': True,
                'message': 'ProductoPersonalizado eliminado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al eliminar el producto'
        }