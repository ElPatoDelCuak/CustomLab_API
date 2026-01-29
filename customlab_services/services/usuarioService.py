from customlab_models.repositories.usuarioRepository import UsuarioRepository

class UsuarioService:
    @staticmethod
    def getUsuarios():
        usuarios = UsuarioRepository.getUsuarios()
        return list(usuarios) or None

    @staticmethod
    def getUsuarioById(idUsuario):
        usuario = UsuarioRepository.getUsuarioById(idUsuario)
        return list(usuario) or None
    
    @staticmethod
    def createUsuario(data):
        new_product = UsuarioRepository.createUsuario(data)
        return {
            'id_usuario': new_product.id_usuario,
            'nombre_usuario': new_product.nombre_usuario,
            'precio_venta': new_product.precio_venta,
            'precio_costo': new_product.precio_costo,
            'stock': new_product.stock,
            'categoria': new_product.categoria,
            'personalizable': new_product.personalizable
        }
    
    @staticmethod
    def updateUsuario(idUsuario, data):
        updated_product = UsuarioRepository.updateUsuario(idUsuario, data)
        if updated_product:
            return {
                'id_usuario': updated_product.id_usuario,
                'nombre_usuario': updated_product.nombre_usuario,
                'precio_venta': updated_product.precio_venta,
                'precio_costo': updated_product.precio_costo,
                'stock': updated_product.stock,
                'categoria': updated_product.categoria,
                'personalizable': updated_product.personalizable
            }
        return None
    
    @staticmethod
    def deleteUsuario(idUsuario):
        usuario = UsuarioRepository.getUsuarioById(idUsuario)
        if usuario:
            UsuarioRepository.deleteUsuario(idUsuario)
            return True
        return False