from customlab_models.repositories.productoRepository import ProductoRepository
from customlab_services.services.imagesService import ImagesService
from customlab_services.services.tallaService import TallaService
class ProductoService:
    @staticmethod
    def getProductos():
        productos = ProductoRepository.getProductos()
        if not productos:
            return {
                'success': False,
                'message': 'No products found'
            }
        for producto in productos:
            producto['images'] = ProductoRepository.getProductImages(producto['id_producto'])
            producto['tallas'] = TallaService.getTallasByProductoId(producto['id_producto'])['data']
        return {
            'success': True,
            'data': productos
        }

    @staticmethod
    def getProductoById(idProducto):
        producto = ProductoRepository.getProductoById(idProducto)
        if not producto:
            return {
                'success': False,
                'message': 'Producto not found'
            }
        producto['images'] = ProductoRepository.getProductImages(idProducto)
        producto['tallas'] = TallaService.getTallasByProductoId(idProducto)['data']
        return {
            'success': True,
            'data': producto
        }

    @staticmethod
    def createProducto(data, images):
        product_name = data.get('nombre_producto')
        upload_type = data.get('upload_type')

        if not images or not product_name or upload_type is None:
            return {
                'success': False,
                'message': 'Product name, images and upload type are required'
            }

        upload_type = int(upload_type)

        for image in images:
            if not ImagesService.verifyImage(image):
                return {
                    'success': False,
                    'message': 'Invalid image format'
                }

        saved_paths = []
        for image in images:
            image_path = ImagesService.saveImage(product_name, upload_type, image)
            if not image_path:
                for path in saved_paths:
                    ImagesService.deleteImage(path)
                return {
                    'success': False,
                    'message': 'Error saving image'
                }
            saved_paths.append(image_path)

        producto = ProductoRepository.createProducto(data)
        if not producto:
            for path in saved_paths:
                ImagesService.deleteImage(path)
            return {
                'success': False,
                'message': 'Error al crear el producto'
            }

        for path in saved_paths:
            ProductoRepository.saveProductImages(producto.id_producto, path)

        return {
            'success': True,
            'message': 'Producto creado exitosamente'
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
        images = ProductoRepository.getProductImages(idProducto)
        for img in images:
            ImagesService.deleteImage(img['ruta'])
        ProductoRepository.deleteProductImages(idProducto)
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