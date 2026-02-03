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
        new_user = UsuarioRepository.createUsuario(data)
        if new_user:
            return True
        return False
    
    @staticmethod
    def updateUsuario(idUsuario, data):
        updated_user = UsuarioRepository.updateUsuario(idUsuario, data)
        if updated_user:
            return True
        return False
    
    @staticmethod
    def deleteUsuario(idUsuario):
        usuario = UsuarioRepository.getUsuarioById(idUsuario)
        if usuario:
            UsuarioRepository.deleteUsuario(idUsuario)
            return True
        return False