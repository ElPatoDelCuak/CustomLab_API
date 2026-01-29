from .core.models import Usuarios
class UsuarioRepository:
    @staticmethod
    def getUsuarios(self):
        return Usuarios.objects.all().values(
            'id_usuario','nombre','apellidos','email','fecha_nacimiento','2fa','rol'
        )
    @staticmethod
    def getUsuarioById(self, idUsuario):
        return Usuarios.objects.filter(id_usuario=idUsuario).values(
            'id_usuario','nombre','apellidos','email','fecha_nacimiento','2fa','rol'
        )
    @staticmethod
    def createUsuario(self, data):
        Usuarios.objects.create(
            nombre=data[1],
            apellidos=data[2],
            email=data[3],
            fecha_nacimiento=data[4],
            twofa=data[5],
            rol=data[6],
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