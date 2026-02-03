from customlab_models.models import Usuarios
class UsuarioRepository:
    @staticmethod
    def getUsuarios():
        return Usuarios.objects.all().values(
            'id_usuario','nombre','apellidos','email','fecha_nacimiento','twofa','rol'
        )
    @staticmethod
    def getUsuarioById(idUsuario):
        return Usuarios.objects.filter(id_usuario=idUsuario).values(
            'id_usuario','nombre','apellidos','email','fecha_nacimiento','twofa','rol'
        )
    @staticmethod
    def createUsuario(data):
        Usuarios.objects.create(
            nombre=data.get('nombre'),
            apellidos=data.get('apellidos'),
            email=data.get('email'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            twofa=data.get('twofa'),
            rol=data.get('rol'),
        )
        return Usuarios.objects.last()
    @staticmethod
    def updateUsuario(idUsuario, data):
        Usuarios.objects.filter(id_usuario=idUsuario).update(
            nombre=data.get('nombre'),
            apellidos=data.get('apellidos'),
            email=data.get('email'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            twofa=data.get('twofa'),
            rol=data.get('rol'),
        )
        return True
    @staticmethod
    def deleteUsuario(idUsuario):
        Usuarios.objects.filter(id_usuario=idUsuario).delete()
        return True