from customlab_models.repositories.productoPersonalizadoRepository import ProductoPersonalizadoRepository
from customlab_services.services.productoService import ProductoService
from customlab_services.services.imagesService import ImagesService
from customlab_services.services.tallaService import TallaService
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
    def createProductoPersonalizado(data, image):
        id_producto = data.get('id_producto')

        if not image or not id_producto:
            return {
                'success': False,
                'message': 'El producto y la imagen son requeridos'
            }
        exist_product = ProductoService.getProductoById(id_producto)
        if not exist_product['success']:
            return {
                'success': False,
                'message': 'El producto no existe'
            }
        if not exist_product['data'].get('personalizable'):
            return {
                'success': False,
                'message': 'El producto no es personalizable'
            }
        exist_talla = TallaService.getTallaById(data.get('id_talla'))
        if not exist_talla['success']:
            return {
                'success': False,
                'message': 'La talla no existe'
            }
        talla_is_from_product = exist_talla['data']['id_producto'] == id_producto
        if not talla_is_from_product:
            return {
                'success': False,
                'message': 'La talla no pertenece al producto'
            }
        if not ImagesService.verifyImage(image):
            return {
                'success': False,
                'message': 'Formato de imagen no válido'
            }
        ruta_imagen = ImagesService.saveImage(id_producto, 2, image)
        if not ruta_imagen:
            return {
                'success': False,
                'message': 'Error al guardar la imagen'
            }
        success = ProductoPersonalizadoRepository.createProductoPersonalizado(data, ruta_imagen)
        if success:
            return {
                'success': True,
                'message': 'ProductoPersonalizado creado exitosamente'
            }
        ImagesService.deleteImage(ruta_imagen)
        return {
            'success': False,
            'message': 'Error al crear el producto'
        }
    
    @staticmethod
    def updateProductoPersonalizado(idProductoPersonalizado, data, image=None):
        exist = ProductoPersonalizadoRepository.getProductoPersonalizadoById(idProductoPersonalizado)
        if not exist:
            return {
                'success': False,
                'message': 'ProductoPersonalizado no encontrado'
            }
        id_producto = data.get('id_producto')
        exist_product = ProductoService.getProductoById(id_producto)
        if not exist_product['success']:
            return {
                'success': False,
                'message': 'El producto no existe'
            }
        if not exist_product['data'].get('personalizable'):
            return {
                'success': False,
                'message': 'El producto no es personalizable'
            }
        exist_talla = TallaService.getTallaById(data.get('id_talla'))
        if not exist_talla['success']:
            return {
                'success': False,
                'message': 'La talla no existe'
            }
        talla_is_from_product = exist_talla['data']['id_producto'] == id_producto
        if not talla_is_from_product:
            return {
                'success': False,
                'message': 'La talla no pertenece al producto'
            }
        ruta_imagen_antigua = exist['ruta_imagen']
        if image:
            if not ImagesService.verifyImage(image):
                return {
                    'success': False,
                    'message': 'Formato de imagen no válido'
                }
            nueva_ruta = ImagesService.saveImage(id_producto, 2, image)
            if not nueva_ruta:
                return {
                    'success': False,
                    'message': 'Error al guardar la imagen'
                }
            data['ruta_imagen'] = nueva_ruta
        else:
            data['ruta_imagen'] = ruta_imagen_antigua
        success = ProductoPersonalizadoRepository.updateProductoPersonalizado(idProductoPersonalizado, data)
        if success:
            if image:
                ImagesService.deleteImage(ruta_imagen_antigua)
            return {
                'success': True,
                'message': 'ProductoPersonalizado actualizado exitosamente'
            }
        if image:
            ImagesService.deleteImage(data['ruta_imagen'])
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
        ImagesService.deleteImage(exist['ruta_imagen'])
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