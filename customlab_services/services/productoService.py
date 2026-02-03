from customlab_models.repositories.productoRepository import ProductoRepository

class ProductoService:
    @staticmethod
    def getProductos():
        productos = ProductoRepository.getProductos()
        return list(productos) or None

    @staticmethod
    def getProductoById(idProducto):
        producto = ProductoRepository.getProductoById(idProducto)
        return list(producto) or None
    
    @staticmethod
    def createProducto(data):
        success = ProductoRepository.createProducto(data)
        if success:
            return {
                'success': True,
                'message': 'Producto creado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al crear el producto'
        }
    
    @staticmethod
    def updateProducto(idProducto, data):
        success = ProductoRepository.updateProducto(idProducto, data)
        if success:
            return {
                'success': True,
                'message': 'Producto actualizado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al actualizar el producto'
        }
    
    @staticmethod
    def deleteProducto(idProducto):
        success = ProductoRepository.deleteProducto(idProducto)
        if success:
            return {
                'success': True,
                'message': 'Producto eliminado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al eliminar el producto'
        }