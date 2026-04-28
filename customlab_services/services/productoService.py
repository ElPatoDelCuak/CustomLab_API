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
        #Get data from request
        # 1. Obtener datos de la request (Formato único: JSON string)
        tallas_raw = data.get('tallas')
        caracteristicas_raw = data.get('caracteristicas')

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
            # Parsear JSON de tallas y características
            tallas = json.loads(tallas_raw) if isinstance(tallas_raw, str) else tallas_raw
            caracteristicas = json.loads(caracteristicas_raw) if isinstance(caracteristicas_raw, str) else caracteristicas_raw
            
            if not isinstance(tallas, list) or not isinstance(caracteristicas, list):
                raise ValueError("Debe ser una lista")
                
            if not tallas or not caracteristicas:
                return {
                    'success': False,
                    'message': 'Se requiere al menos una talla y una característica'
                }
        except (json.JSONDecodeError, ValueError, TypeError):
            return {
                'success': False,
                'message': 'Error al procesar el formato de tallas o características. Deben enviarse como un array JSON string.'
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
    def updateProducto(idProducto, json_data, new_images=None):
        try:
            # Si json_data es un string, lo parseamos
            data = json.loads(json_data) if isinstance(json_data, str) else json_data
            
            # 1. Actualizar datos base del Producto
            producto_data = data.get('producto', {})
            if producto_data:
                ProductoRepository.updateProducto(idProducto, producto_data)

            # 2. Gestionar Tallas
            tallas_data = data.get('tallas', {})
            if tallas_data:
                # Borrar tallas
                for id_talla in tallas_data.get('tallas_to_delete', []):
                    TallaRepository.deleteTalla(id_talla)
                
                # Crear nuevas tallas
                for talla_new in tallas_data.get('tallas_to_upload', []):
                    talla_new['id_producto'] = idProducto
                    TallaService.createTalla(talla_new)
                
                # Modificar tallas existentes
                for talla_mod in tallas_data.get('tallas_to_modify', []):
                    id_talla = talla_mod.get('id_talla')
                    if id_talla:
                        talla_mod['id_producto'] = idProducto
                        TallaRepository.updateTalla(id_talla, talla_mod)

            # 3. Gestionar Características
            carac_data = data.get('caracteristicas', {})
            if carac_data:
                # Eliminar asociaciones
                for id_carac in carac_data.get('caracteristicas_to_delete', []):
                    CaracteristicaRepository.removeCaracteristicaFromProducto(idProducto, id_carac)
                
                # Añadir nuevas asociaciones
                for id_carac in carac_data.get('caracteristicas_to_upload', []):
                    CaracteristicaRepository.addCaracteristicaToProducto(idProducto, id_carac)

            # 4. Gestionar Imágenes
            img_data = data.get('imagenes', {})
            if img_data:
                # Borrar imágenes específicas
                for id_img in img_data.get('imagenes_to_delete', []):
                    from customlab_services.services.productImagesService import ProductImagesService
                    ProductImagesService.deleteProductImageById(id_img)

            # Subir nuevas imágenes si existen
            if new_images:
                upload_type = 3
                for img in new_images:
                    if ImagesService.verifyImage(img):
                        path = ImagesService.saveImage(idProducto, upload_type, img)
                        if path:
                            ProductImagesRepository.saveProductImages(idProducto, path)

            return {
                'success': True,
                'message': 'Producto actualizado de forma integral'
            }

        except Exception as e:
            return {
                'success': False,
                'message': f'Error en la actualización integral: {str(e)}'
            }
    
    @staticmethod
    def deleteProducto(idProducto):
        exist = ProductoRepository.getProductoById(idProducto)
        if not exist:
            return {
                'success': False,
                'message': 'Producto no encontrado'
            }
        #Delete images files
        images = ProductImagesRepository.getProductImagesByProductId(idProducto)
        for img in images:
            ImagesService.deleteImage(img['ruta'])
        
        #Delete asociated data
        ProductImagesRepository.deleteProductImages(idProducto)
        TallaRepository.deleteTallasByProductoId(idProducto)
        CaracteristicaRepository.removeCaracteristicasByProductoId(idProducto)
        
        #Delete product
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