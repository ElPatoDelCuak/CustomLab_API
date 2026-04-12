from customlab_models.repositories.productoRepository import ProductoRepository
from customlab_models.repositories.productImagesRepository import ProductImagesRepository
from customlab_services.services.imagesService import ImagesService
from customlab_services.services.tallaService import TallaService
import random
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
            producto['images'] = ProductImagesRepository.getProductImagesByProductId(producto['id_producto'])
            producto['tallas'] = TallaService.getTallasByProductoId(producto['id_producto'])['data']
            if not producto['images']:
                return {
                    'success': False,
                    'message': 'Error retrieving product images'
                }
            if not producto['tallas']:
                return {
                    'success': False,
                    'message': 'Error retrieving product sizes'
                }
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
        producto['images'] = ProductImagesRepository.getProductImagesByProductId(idProducto)
        producto['tallas'] = TallaService.getTallasByProductoId(idProducto)['data']
        return {
            'success': True,
            'data': producto
        }
    
    @staticmethod
    def getFeaturedProducts():
        productos = ProductoRepository.getProductos()
        if not productos:
            return {
                'success': False,
                'message': 'No products found'
            }
        featured = [p for p in productos if p['nuevo'] or p['oferta'] or p['personalizable']]
        if not featured:
            return {
            'success': False,
            'message': 'No featured products found'
            }
        if len(featured) > 3:
            featured = random.sample(featured, 3)
        for producto in featured:
            producto['images'] = ProductImagesRepository.getProductImagesByProductId(producto['id_producto'])
            producto['tallas'] = TallaService.getTallasByProductoId(producto['id_producto'])['data']
            if not producto['images']:
                return {
                    'success': False,
                    'message': 'Error retrieving product images'
                }
            if not producto['tallas']:
                return {
                    'success': False,
                    'message': 'Error retrieving product sizes'
                }
        return {
            'success': True,
            'data': featured
        }

    @staticmethod
    def createProducto(data, images):
        product_name = data.get('nombre_producto')

        if not images or not product_name:
            return {
                'success': False,
                'message': 'Product name and images are required'
            }

        upload_type = 3

        for image in images:
            if not ImagesService.verifyImage(image):
                return {
                    'success': False,
                    'message': 'Invalid image format'
                }

        producto = ProductoRepository.createProducto(data)
        if not producto:
            return {
                'success': False,
                'message': 'Error al crear el producto'
            }

        saved_paths = []
        for image in images:
            image_path = ImagesService.saveImage(producto.id_producto, upload_type, image)
            if not image_path:
                for path in saved_paths:
                    ImagesService.deleteImage(path)
                ProductoRepository.deleteProducto(producto.id_producto)
                return {
                    'success': False,
                    'message': 'Error saving image'
                }
            saved_paths.append(image_path)

        for path in saved_paths:
            saved = ProductImagesRepository.saveProductImages(producto.id_producto, path)
            if not saved:
                for image_path in saved_paths:
                    ImagesService.deleteImage(image_path)
                ProductImagesRepository.deleteProductImages(producto.id_producto)
                ProductoRepository.deleteProducto(producto.id_producto)
                return {
                    'success': False,
                    'message': 'Error saving image metadata'
                }

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
        images = ProductImagesRepository.getProductImagesByProductId(idProducto)
        for img in images:
            ImagesService.deleteImage(img['ruta'])
        ProductImagesRepository.deleteProductImages(idProducto)
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