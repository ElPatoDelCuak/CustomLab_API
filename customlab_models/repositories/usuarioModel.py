from .core.models import Usuarios
class UsuarioModel:
    @staticmethod
    def getUsuarios(self):
        return Usuarios.objects.all().values(
            
        )
    @staticmethod
    def getUsuarioById(self, idUsuario):
        return Usuarios.objects.filter(id_usuario=idUsuario).values(

        )
    @staticmethod
    def createUsuario(self, data):
        Usuarios.objects.create(

        )
        return Usuarios.objects.last()
    @staticmethod
    def updateUsuario(self, idUsuario, data):
        Usuarios.objects.filter(id_usuario=idUsuario).update(

        )
        return Usuarios.objects.get(id_usuario=idUsuario)
    @staticmethod
    def deleteUsuario(self, idUsuario):
        Usuarios.objects.filter(id_usuario=idUsuario).delete()
        return Usuarios.objects.get(id_usuario=idUsuario)