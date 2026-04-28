from customlab_services.services.imagesService import ImagesService
from customlab_services.services.productoService import ProductoService
from customlab_models.repositories.productImagesRepository import ProductImagesRepository

class ProductImagesService:
    @staticmethod
    def getProductImagesByProductId(id_producto):
        product_exist = ProductoService.getProductoById(id_producto)
        if not product_exist['success']:
            return {
                'success': False,
                'message': 'Producto not found'
            }
        
        images = ProductImagesRepository.getProductImagesByProductId(id_producto)
        return {
            'success': True,
            'data': images
        }

    @staticmethod
    def uploadProductImage(id_producto, images):

        product_exist = ProductoService.getProductoById(id_producto)
        
        if not images or not id_producto:
            return {
                'success': False,
                'message': 'Product name and images are required'
            }
        
        if not product_exist['success']:
            return {
                'success': False,
                'message': 'Producto not found'
            }
        
        # Product images always go to products folder.
        upload_type = 3

        for img in images:
            if not ImagesService.verifyImage(img):
                return {
                    'success': False,
                    'message': 'Invalid image format'
                }

        saved_paths = []
        for img in images:
            image_path = ImagesService.saveImage(id_producto, upload_type, img)
            if not image_path:
                for path in saved_paths:
                    ImagesService.deleteImage(path)
                return {
                    'success': False,
                    'message': 'Error saving image'
                }
            saved_paths.append(image_path)

        for path in saved_paths:
            saved = ProductImagesRepository.saveProductImages(id_producto, path)
            if not saved:
                for image_path in saved_paths:
                    ImagesService.deleteImage(image_path)
                ProductImagesRepository.deleteProductImages(id_producto)
                return {
                    'success': False,
                    'message': 'Error saving image metadata'
                }

        return {
            'success': True,
            'message': 'Imágenes del producto creadas exitosamente'
        }
    
    @staticmethod
    def deleteProductImage(id_producto):
        images = ProductImagesRepository.getProductImagesByProductId(id_producto)
        if not images:
            return {
                'success': False,
                'message': 'Producto not found'
            }
        
        for img in images:
            ImagesService.deleteImage(img['ruta'])
        
        ProductImagesRepository.deleteProductImages(id_producto)
        return {
            'success': True,
            'message': 'Imágenes del producto eliminadas exitosamente'
        }

    @staticmethod
    def deleteProductImageById(id_imagen):
        image = ProductImagesRepository.getProductImageById(id_imagen)
        if not image:
            return {
                'success': False,
                'message': 'Imagen no encontrada'
            }
        
        # 1. Borrar archivo físico
        ImagesService.deleteImage(image['ruta'])
        
        # 2. Borrar de la base de datos
        success = ProductImagesRepository.deleteProductImageById(id_imagen)
        
        if success:
            return {
                'success': True,
                'message': 'Imagen eliminada exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al eliminar la imagen de la base de datos'
        }