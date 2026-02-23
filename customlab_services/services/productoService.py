from customlab_models.repositories.productoRepository import ProductoRepository
from customlab_services.services.imagesService import ImagesService
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
    def createProducto(data, images):
        product_name = data.get('nombre_producto')
        upload_type = int(data.get('upload_type'))
        if not images or not product_name or not upload_type:
            return {
                'success': False,
                'message': 'Product name, images and upload type are required'
            }
        for image in images:
            if not ImagesService.verifyImage(image):
                return {
                    'success': False,
                    'message': 'Invalid image format'
                }
            if not ImagesService.saveImage(product_name, upload_type, image):
                return {
                    'success': False,
                    'message': 'Error saving image'
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
    @staticmethod
    def verifyProducto(data):
        pass
    @staticmethod
    def verifyUpdateProducto(data):
        pass
    @staticmethod
    def verificarStockProducto(idProducto, cantidad):
        pass