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
    def getUsuarioPasswordById(idUsuario):
        usuario = Usuarios.objects.filter(id_usuario=idUsuario).values('password').first()
        return usuario['password'] if usuario else None

    @staticmethod
    def getUsuarioByEmail(email):
        return Usuarios.objects.filter(email__iexact=email).values(
            'id_usuario','nombre','apellidos','email','password','fecha_nacimiento','doble_factor','rol'
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
        # Campos permitidos para actualización general (excluimos password)
        update_fields = {}
        allowed_fields = ['nombre', 'apellidos', 'email', 'fecha_nacimiento', 'doble_factor', 'rol']
        
        for field in allowed_fields:
            if field in data:
                update_fields[field] = data.get(field)

        if not update_fields:
            return False

        updated_rows = Usuarios.objects.filter(id_usuario=idUsuario).update(**update_fields)
        return updated_rows > 0
    
    @staticmethod
    def updatePassword(idUsuario, hashed_password):
        updated_rows = Usuarios.objects.filter(id_usuario=idUsuario).update(
            password=hashed_password
        )
        return updated_rows > 0
    
    @staticmethod
    def deleteUsuario(idUsuario):
        deleted_rows, _ = Usuarios.objects.filter(id_usuario=idUsuario).delete()
        return deleted_rows > 0