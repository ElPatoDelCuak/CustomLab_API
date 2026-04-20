from customlab_models.repositories.carritoRepository import CarritoRepository
from customlab_models.repositories.productoRepository import ProductoRepository
from customlab_models.repositories.usuarioRepository import UsuarioRepository


class CarritoService:
    @staticmethod
    def getCarritoByUserId(id_usuario):
        # Verificar que el usuario existe
        usuario = UsuarioRepository.getUsuarioById(id_usuario)
        if not usuario:
            return {
                'success': False,
                'message': 'Usuario no encontrado'
            }

        carrito = CarritoRepository.getCarritoByUserId(id_usuario)
        if carrito is False:
            return {
                'success': True,
                'data': []
            }

        # Enriquecer con información del producto
        carrito_enriquecido = []
        for item in carrito:
            producto = ProductoRepository.getProductoById(item['id_producto'])
            if producto:
                item_enriquecido = {
                    'id_usuario': item['id_usuario'],
                    'id_producto': item['id_producto'],
                    'cantidad': item['cantidad'],
                    'precio_total': float(item['precio_total']),
                    'producto': {
                        'nombre_producto': producto['nombre_producto'],
                        'precio_venta': float(producto['precio_venta']),
                        'stock': producto['stock'],
                        'categoria': producto['categoria']
                    }
                }
                carrito_enriquecido.append(item_enriquecido)

        return {
            'success': True,
            'data': carrito_enriquecido
        }

    @staticmethod
    def addItemToCarrito(id_usuario, id_producto, cantidad):
        # Verificar que el usuario existe
        usuario = UsuarioRepository.getUsuarioById(id_usuario)
        if not usuario:
            return {
                'success': False,
                'message': 'Usuario no encontrado'
            }

        # Verificar que el producto existe
        producto = ProductoRepository.getProductoById(id_producto)
        if not producto:
            return {
                'success': False,
                'message': 'Producto no encontrado'
            }

        # Verificar stock
        if cantidad > producto['stock']:
            return {
                'success': False,
                'message': 'Cantidad solicitada supera el stock disponible'
            }

        # Calcular precio total
        precio_total = float(producto['precio_venta']) * cantidad

        # Verificar si el item ya existe en el carrito
        existing_item = CarritoRepository.getCarritoItem(id_usuario, id_producto)
        if existing_item:
            # Actualizar cantidad y precio total
            nueva_cantidad = existing_item['cantidad'] + cantidad
            if nueva_cantidad > producto['stock']:
                return {
                    'success': False,
                    'message': 'Cantidad total supera el stock disponible'
                }
            nuevo_precio_total = float(producto['precio_venta']) * nueva_cantidad
            success = CarritoRepository.updateCarritoItem(id_usuario, id_producto, nueva_cantidad, nuevo_precio_total)
        else:
            # Crear nuevo item
            success = CarritoRepository.createCarritoItem(id_usuario, id_producto, cantidad, precio_total)

        if success:
            return {
                'success': True,
                'message': 'Producto agregado al carrito exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al agregar producto al carrito'
        }

    @staticmethod
    def updateCarritoItem(id_usuario, id_producto, cantidad):
        # Verificar que el usuario existe
        usuario = UsuarioRepository.getUsuarioById(id_usuario)
        if not usuario:
            return {
                'success': False,
                'message': 'Usuario no encontrado'
            }

        # Verificar que el producto existe
        producto = ProductoRepository.getProductoById(id_producto)
        if not producto:
            return {
                'success': False,
                'message': 'Producto no encontrado'
            }

        # Verificar stock
        if cantidad > producto['stock']:
            return {
                'success': False,
                'message': 'Cantidad solicitada supera el stock disponible'
            }

        # Verificar que el item existe en el carrito
        existing_item = CarritoRepository.getCarritoItem(id_usuario, id_producto)
        if not existing_item:
            return {
                'success': False,
                'message': 'Producto no encontrado en el carrito'
            }

        if cantidad <= 0:
            # Si cantidad es 0 o negativa, eliminar el item
            success = CarritoRepository.deleteCarritoItem(id_usuario, id_producto)
            message = 'Producto eliminado del carrito'
        else:
            # Actualizar cantidad y precio total
            precio_total = float(producto['precio_venta']) * cantidad
            success = CarritoRepository.updateCarritoItem(id_usuario, id_producto, cantidad, precio_total)
            message = 'Producto actualizado en el carrito'

        if success:
            return {
                'success': True,
                'message': message
            }
        return {
            'success': False,
            'message': 'Error al actualizar el carrito'
        }

    @staticmethod
    def removeItemFromCarrito(id_usuario, id_producto):
        # Verificar que el usuario existe
        usuario = UsuarioRepository.getUsuarioById(id_usuario)
        if not usuario:
            return {
                'success': False,
                'message': 'Usuario no encontrado'
            }

        # Verificar que el item existe en el carrito
        existing_item = CarritoRepository.getCarritoItem(id_usuario, id_producto)
        if not existing_item:
            return {
                'success': False,
                'message': 'Producto no encontrado en el carrito'
            }

        success = CarritoRepository.deleteCarritoItem(id_usuario, id_producto)
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
        # Verificar que el usuario existe
        usuario = UsuarioRepository.getUsuarioById(id_usuario)
        if not usuario:
            return {
                'success': False,
                'message': 'Usuario no encontrado'
            }

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