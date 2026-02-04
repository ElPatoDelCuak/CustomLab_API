from customlab_models.repositories.productoRepository import ProductoRepository

class ProductoService:
    @staticmethod
    def getProductos():
        productos = ProductoRepository.getProductos()
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
    def getProductoById(idProducto):
        producto = ProductoRepository.getProductoById(idProducto)
        if producto:
            return {
                'success': True,
                'data': producto
            }
        return {
            'success': False,
            'message': 'Producto not found'
        }

    @staticmethod
    def createProducto(data):
        exist = ProductoRepository.getProductoById(data.get('id_producto'))
        if exist:
            return {
                'success': False,
                'message': 'El producto ya existe'
            }
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
        exist = ProductoRepository.getProductoById(idProducto)
        if not exist:
            return {
                'success': False,
                'message': 'Producto no encontrado'
            }
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
        exist = ProductoRepository.getProductoById(idProducto)
        if not exist:
            return {
                'success': False,
                'message': 'Producto no encontrado'
            }
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