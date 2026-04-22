from customlab_models.repositories.carritoRepository import CarritoRepository
from customlab_services.services.productoService import ProductoService
from customlab_services.services.usuarioService import UsuarioService
from customlab_services.services.tallaService import TallaService


class CarritoService:
    @staticmethod
    def getCarritoByUserId(id_usuario):
        user_exists = UsuarioService.getUsuarioById(id_usuario)
        if not user_exists['success']:
            return user_exists

        carrito = CarritoRepository.getCarritoByUserId(id_usuario)
        if carrito is False:
            return {'success': True, 'data': []}

        carrito_enriquecido = []
        for item in carrito:
            producto_res = ProductoService.getProductoById(item['id_producto'])
            talla_res = TallaService.getTallaById(item['id_talla'])
            
            if producto_res['success'] and talla_res['success']:
                producto_data = producto_res['data']
                talla_data = talla_res['data']
                
                item_enriquecido = {
                    'id_usuario': item['id_usuario'],
                    'id_producto': item['id_producto'],
                    'id_talla': item['id_talla'],
                    'cantidad': item['cantidad'],
                    'precio_total': float(item['precio_total']),
                    'producto': {
                        'nombre_producto': producto_data['nombre_producto'],
                        'precio_unitario': float(producto_data['precio_venta']),
                        'imagen': producto_data['images'][0]['ruta'] if producto_data['images'] else None,
                        'categoria': producto_data['categoria']
                    },
                    'talla': {
                        'nombre': talla_data['talla']
                    }
                }
                carrito_enriquecido.append(item_enriquecido)

        return {
            'success': True,
            'data': carrito_enriquecido
        }

    @staticmethod
    def addItemToCarrito(id_usuario, id_producto, id_talla, cantidad):
        user_res = UsuarioService.getUsuarioById(id_usuario)
        if not user_res['success']:
            return user_res

        product_res = ProductoService.getProductoById(id_producto)
        if not product_res['success']:
            return product_res

        producto_data = product_res['data']
        
        talla_res = TallaService.getTallaById(id_talla)
        if not talla_res['success']:
            return talla_res
        
        talla_data = talla_res['data']
        if talla_data['id_producto'] != id_producto:
            return {
                'success': False,
                'message': 'La talla seleccionada no pertenece a este producto'
            }

        if cantidad > talla_data['stock']:
            return {
                'success': False,
                'message': f'Cantidad solicitada ({cantidad}) supera el stock disponible de la talla ({talla_data["stock"]})'
            }
        
        if cantidad <= 0:
            return {
                'success': False,
                'message': 'La cantidad debe ser mayor a 0'
            }

        product_price = producto_data['precio_venta']

        exist_item = CarritoRepository.getCarritoItem(id_usuario, id_producto, id_talla)
        
        if exist_item:
            if exist_item['cantidad'] + cantidad > talla_data['stock']:
                return {
                    'success': False,
                    'message': 'La cantidad total superaría el stock disponible'
                }
            exito = CarritoRepository.incrementarCantidad(id_usuario, id_producto, id_talla, cantidad, product_price)
        else:
            total_price = product_price * cantidad
            exito = CarritoRepository.createCarritoItem(id_usuario, id_producto, id_talla, cantidad, total_price)

        if exito:
            return {
                'success': True,
                'message': 'Producto agregado al carrito exitosamente'
            }
        
        return {
            'success': False,
            'message': 'Error al procesar la solicitud en el carrito'
        }

    @staticmethod
    def updateCarritoItem(id_usuario, id_producto, id_talla, cantidad):
        user_res = UsuarioService.getUsuarioById(id_usuario)
        if not user_res['success']:
            return user_res

        product_res = ProductoService.getProductoById(id_producto)
        if not product_res['success']:
            return product_res
        
        producto_data = product_res['data']

        talla_res = TallaService.getTallaById(id_talla)
        if not talla_res['success']:
            return talla_res
            
        talla_data = talla_res['data']

        if talla_data['id_producto'] != id_producto:
             return {
                'success': False,
                'message': 'La talla seleccionada no pertenece a este producto'
            }

        exist_item = CarritoRepository.getCarritoItem(id_usuario, id_producto, id_talla)
        if not exist_item:
            return {
                'success': False,
                'message': 'Producto con esa talla no encontrado en el carrito'
            }

        if cantidad <= 0:
            exito = CarritoRepository.deleteCarritoItem(id_usuario, id_producto, id_talla)
            message = 'Producto eliminado del carrito'
        elif cantidad == exist_item['cantidad']:
            return {
                'success': True,
                'message': 'La cantidad es la misma que ya existe en el carrito'
            }
        else:
            if cantidad > talla_data['stock']:
                return {
                    'success': False,
                    'message': f'Cantidad solicitada ({cantidad}) supera el stock disponible de la talla ({talla_data["stock"]})'
                }
                
            product_price = producto_data['precio_venta']
            nuevo_precio_total = product_price * cantidad
            exito = CarritoRepository.updateCarritoItem(id_usuario, id_producto, id_talla, cantidad, nuevo_precio_total)
            message = 'Carrito actualizado exitosamente'

        if exito:
            return {
                'success': True,
                'message': message
            }
        
        return {
            'success': False,
            'message': 'Error al procesar la actualización del carrito'
        }
            
    @staticmethod
    def removeItemFromCarrito(id_usuario, id_producto, id_talla):
        user_res = UsuarioService.getUsuarioById(id_usuario)
        if not user_res['success']:
            return user_res
            
        exist_item = CarritoRepository.getCarritoItem(id_usuario, id_producto, id_talla)
        if not exist_item:
            return {
                'success': False,
                'message': 'Producto con esa talla no encontrado en el carrito'
            }
            
        success = CarritoRepository.deleteCarritoItem(id_usuario, id_producto, id_talla)
        if success:
            return {
                'success': True,
                'message': 'Producto eliminado del carrito exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al eliminar producto del carrito'
        }

    @staticmethod
    def clearCarrito(id_usuario):
        user_res = UsuarioService.getUsuarioById(id_usuario)
        if not user_res['success']:
            return user_res
            
        success = CarritoRepository.clearCarritoByUserId(id_usuario)
        if success:
            return {
                'success': True,
                'message': 'Carrito vaciado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al vaciar el carrito'
        }