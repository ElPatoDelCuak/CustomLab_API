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
    def getUsuarioByEmail(email):
        return Usuarios.objects.filter(email__iexact=email).values(
            'id_usuario',
            'nombre',
            'apellidos',
            'email',
            'password',
            'fecha_nacimiento',
            'doble_factor',
            'rol'
        ).first()

    @staticmethod
    def createUsuario(data):
        user = Usuarios.objects.create(
            nombre=data.get('nombre'),
            apellidos=data.get('apellidos'),
            email=data.get('email'),
            password=data.get('password'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            doble_factor=data.get('doble_factor'),
            rol=data.get('rol'),
        )
        return user is not None
    
    @staticmethod
    def updateUsuario(idUsuario, data):
        updated_rows = Usuarios.objects.filter(id_usuario=idUsuario).update(
            nombre=data.get('nombre'),
            apellidos=data.get('apellidos'),
            email=data.get('email'),
            password=data.get('password'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            doble_factor=data.get('doble_factor'),
            rol=data.get('rol'),
        )
        return updated_rows > 0
    
    @staticmethod
    def deleteUsuario(idUsuario):
        deleted_rows, _ = Usuarios.objects.filter(id_usuario=idUsuario).delete()
        return deleted_rows > 0