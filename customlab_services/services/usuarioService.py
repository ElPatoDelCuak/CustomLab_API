from customlab_models.repositories.usuarioRepository import UsuarioRepository

class UsuarioService:
    @staticmethod
    def getUsuarios():
        usuarios = UsuarioRepository.getUsuarios()
        if usuarios:
            return {
                'success': True,
                'data': list(usuarios)
            }
        return {
            'success': False,
            'message': 'No users found'
        }

    @staticmethod
    def getUsuarioById(idUsuario):
        usuario = UsuarioRepository.getUsuarioById(idUsuario)
        if usuario:
            return {
                'success': True,
                'data': usuario
            }
        return {
            'success': False,
            'message': 'Usuario not found'
        }
    
    @staticmethod
    def createUsuario(data):
        success = UsuarioRepository.createUsuario(data)
        if success:
            return {
                'success': True,
                'message': 'Usuario creado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al crear el usuario'
        }
    
    @staticmethod
    def updateUsuario(idUsuario, data):
        success = UsuarioRepository.updateUsuario(idUsuario, data)
        if success:
            return {
                'success': True,
                'message': 'Usuario actualizado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al actualizar el usuario'
        }
    
    @staticmethod
    def deleteUsuario(idUsuario):
        user = UsuarioRepository.getUsuarioById(idUsuario)
        if not user:
            return False
        success = UsuarioRepository.deleteUsuario(idUsuario)
        if success:
            return {
                'success': True,
                'message': 'Usuario eliminado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al eliminar el usuario'
        }