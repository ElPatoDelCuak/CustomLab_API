from customlab_models.repositories.productoRepository import ProductoRepository
from customlab_models.repositories.productImagesRepository import ProductImagesRepository
from customlab_models.repositories.tallaRepository import TallaRepository
from customlab_models.repositories.caracteristicaRepository import CaracteristicaRepository
from customlab_services.services.caracteristicaService import CaracteristicaService
from customlab_services.services.imagesService import ImagesService
from customlab_services.services.tallaService import TallaService
import random
import json
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
            if not producto['images']:
                return {
                    'success': False,
                    'message': 'Error retrieving product images'
                }
            producto['tallas'] = TallaService.getTallasByProductoId(producto['id_producto'])['data']
            if not producto['tallas']:
                return {
                    'success': False,
                    'message': 'Error retrieving product sizes'
                }
            producto['caracteristicas'] = CaracteristicaService.getCaracteristicasByProducto(producto['id_producto']).get('data', [])
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
        if not producto['images']:
            return {
                'success': False,
                'message': 'Error retrieving product images'
            }
        producto['tallas'] = TallaService.getTallasByProductoId(idProducto)['data']
        if not producto['tallas']:
            return {
                'success': False,
                'message': 'Error retrieving product sizes'
            }   
        producto['caracteristicas'] = CaracteristicaService.getCaracteristicasByProducto(idProducto).get('data', [])
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
            producto['caracteristicas'] = CaracteristicaService.getCaracteristicasByProducto(producto['id_producto']).get('data', [])
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
        tallas_raw = data.get('tallas')
        caracteristicas_raw = data.get('caracteristicas')

        # 1. Validaciones iniciales
        if not images or not product_name:
            return {
                'success': False,
                'message': 'El nombre del producto y las imágenes son obligatorios'
            }

        if not tallas_raw or not caracteristicas_raw:
            return {
                'success': False,
                'message': 'Las tallas y características son obligatorias'
            }

        try:
            tallas = json.loads(tallas_raw) if isinstance(tallas_raw, str) else tallas_raw
            caracteristicas = json.loads(caracteristicas_raw) if isinstance(caracteristicas_raw, str) else caracteristicas_raw
        except Exception:
            return {
                'success': False,
                'message': 'Error al procesar el formato de tallas o características'
            }

        if not tallas or not caracteristicas:
            return {
                'success': False,
                'message': 'Se requiere al menos una talla y una característica'
            }

        # 2. Verificar formato de imágenes
        for image in images:
            if not ImagesService.verifyImage(image):
                return {
                    'success': False,
                    'message': 'Formato de imagen inválido'
                }

        # 3. Crear el producto base
        producto = ProductoRepository.createProducto(data)
        if not producto:
            return {
                'success': False,
                'message': 'Error al crear el producto'
            }

        # 4. Procesar Imágenes
        upload_type = 3
        saved_paths = []
        for image in images:
            image_path = ImagesService.saveImage(producto.id_producto, upload_type, image)
            if not image_path:
                ProductoService.deleteProducto(producto.id_producto)
                return {'success': False, 'message': 'Error al guardar el archivo de imagen'}
            saved_paths.append(image_path)

        for path in saved_paths:
            saved = ProductImagesRepository.saveProductImages(producto.id_producto, path)
            if not saved:
                ProductoService.deleteProducto(producto.id_producto)
                return {'success': False, 'message': 'Error al registrar la imagen en la base de datos'}

        # 5. Procesar Tallas
        for talla_data in tallas:
            talla_data['id_producto'] = producto.id_producto
            success = TallaService.createTalla(talla_data)
            if not success['success']:
                ProductoService.deleteProducto(producto.id_producto)
                return {'success': False, 'message': f'Error al crear la talla: {success.get("message")}'}

        # 6. Procesar Características
        for carac_data in caracteristicas:
            # carac_data puede ser un ID directo o un objeto {"id_caracteristica": ID}
            id_carac = carac_data.get('id_caracteristica') if isinstance(carac_data, dict) else carac_data
            success = CaracteristicaService.addCaracteristicaToProducto(producto.id_producto, id_carac)
            if not success['success']:
                ProductoService.deleteProducto(producto.id_producto)
                return {'success': False, 'message': f'Error al asociar la característica: {success.get("message")}'}

        return {
            'success': True,
            'message': 'Producto creado exitosamente con sus tallas y características'
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
        
        # 1. Eliminar archivos físicos de imágenes
        images = ProductImagesRepository.getProductImagesByProductId(idProducto)
        for img in images:
            ImagesService.deleteImage(img['ruta'])
        
        # 2. Eliminar registros de imágenes en BD
        ProductImagesRepository.deleteProductImages(idProducto)
        
        # 3. Eliminar tallas relacionadas
        TallaRepository.deleteTallasByProductoId(idProducto)
        
        # 4. Eliminar asociaciones de características
        CaracteristicaRepository.removeCaracteristicasByProductoId(idProducto)
        
        # 5. Eliminar el producto final
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