from customlab_models.models import Usuarios
class UsuarioRepository:
    @staticmethod
    def getUsuarios():
        usuarios = Usuarios.objects.all().values(
            'id_usuario','nombre','apellidos','email','fecha_nacimiento','doble_factor','rol'
        )
        if not usuarios.exists():
            return False
        return usuarios
    
    @staticmethod
    def getUsuarioById(idUsuario):
        usuario = Usuarios.objects.filter(id_usuario=idUsuario).values(
            'id_usuario','nombre','apellidos','email','fecha_nacimiento','doble_factor','rol'
        )
        if not usuario.exists():
            return False
        return usuario

    @staticmethod
    def createUsuario(data):
        Usuarios.objects.create(
            nombre=data.get('nombre'),
            apellidos=data.get('apellidos'),
            email=data.get('email'),
            password=data.get('password'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            doble_factor=data.get('doble_factor'),
            rol=data.get('rol'),
        )
        if Usuarios.objects.exists():
            return True
        return False
    
    @staticmethod
    def updateUsuario(idUsuario, data):
        Usuarios.objects.filter(id_usuario=idUsuario).update(
            nombre=data.get('nombre'),
            apellidos=data.get('apellidos'),
            email=data.get('email'),
            password=data.get('password'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            doble_factor=data.get('doble_factor'),
            rol=data.get('rol'),
        )
        if Usuarios.objects.filter(id_usuario=idUsuario).exists():
            return True
        return False
    
    @staticmethod
    def deleteUsuario(idUsuario):
        Usuarios.objects.filter(id_usuario=idUsuario).delete()
        if not Usuarios.objects.filter(id_usuario=idUsuario).exists():
            return True
        return False