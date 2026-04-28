from customlab_models.repositories.usuarioRepository import UsuarioRepository
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

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
        payload = dict(data)
        payload['email'] = UsuarioService.normalize_email(payload.get('email'))
        payload['rol'] = payload.get('rol', 'cliente')

        if not payload.get('email'):
            return {
                'success': False,
                'message': 'El email es obligatorio'
            }

        try:
            payload['password'] = UsuarioService.validate_and_hash_password(payload.get('password'))
        except ValidationError as exc:
            return {
                'success': False,
                'message': '; '.join(exc.messages)
            }
        
        email_duplicated = UsuarioRepository.getUsuarioByEmail(payload['email'])
        if email_duplicated:
            return {
                'success': False,
                'message': 'El email ya esta registrado'
            }

        success = UsuarioRepository.createUsuario(payload)
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
        payload = dict(data)
        
        # El email es opcional en la actualización, pero si viene lo normalizamos
        if 'email' in payload:
            payload['email'] = UsuarioService.normalize_email(payload.get('email'))
            if not payload['email']:
                return {
                    'success': False,
                    'message': 'El email no puede estar vacío'
                }
            
            # Verificar si el nuevo email ya está en uso por otro usuario
            email_duplicated = UsuarioRepository.getUsuarioByEmail(payload['email'])
            if email_duplicated and email_duplicated['id_usuario'] != idUsuario:
                return {
                    'success': False,
                    'message': 'El email ya esta registrado'
                }
        success = UsuarioRepository.updateUsuario(idUsuario, payload)
        if success:
            return {
                'success': True,
                'message': 'Usuario actualizado exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al actualizar el usuario o no hubo cambios'
        }
    
    @staticmethod
    def updatePassword(idUsuario, old_password, new_password):
        stored_password = UsuarioRepository.getUsuarioPasswordById(idUsuario)
        if not stored_password:
            return {'success': False, 'message': 'Usuario no encontrado'}
        
        if not check_password(str(old_password), stored_password):
            return {'success': False, 'message': 'La contraseña antigua es incorrecta'}
        
        try:
            hashed_password = UsuarioService.validate_and_hash_password(new_password)
        except ValidationError as exc:
            return {'success': False, 'message': '; '.join(exc.messages)}
            
        success = UsuarioRepository.updatePassword(idUsuario, hashed_password)
        if success:
            return {'success': True, 'message': 'Contraseña actualizada exitosamente'}
        return {'success': False, 'message': 'Error al actualizar la contraseña'}
    
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
        
    @staticmethod
    def normalize_email(email):
        if email is None:
            return None
        return str(email).strip().lower()

    @staticmethod
    def validate_and_hash_password(password):
        if password is None:
            raise ValidationError('La password es obligatoria')

        plain_password = str(password).strip()
        if not plain_password:
            raise ValidationError('La password no puede estar vacia')

        validate_password(plain_password)
        return make_password(plain_password)

    @staticmethod
    def verifyUsuario(data):
        email = UsuarioService.normalize_email(data.get('email'))
        password = data.get('password')

        if not email or not password:
            return {
                'success': False,
                'message': 'Email y password son obligatorios'
            }

        usuario = UsuarioRepository.getUsuarioByEmail(email)
        if not usuario:
            return {
                'success': False,
                'message': 'Credenciales invalidas'
            }

        stored_password = usuario.get('password')
        valid_password = check_password(str(password), stored_password)
        if not valid_password:
            return {
                'success': False,
                'message': 'Credenciales invalidas'
            }

        refresh = RefreshToken()
        refresh['id_usuario'] = usuario['id_usuario']
        refresh['email'] = usuario['email']
        refresh['rol'] = usuario['rol']

        return {
            'success': True,
            'message': 'Login exitoso',
            'data': {
                'usuario': {
                    'id_usuario': usuario['id_usuario'],
                    'nombre': usuario['nombre'],
                    'apellidos': usuario['apellidos'],
                    'email': usuario['email'],
                    'rol': usuario['rol'],
                    'doble_factor': usuario['doble_factor'],
                },
                'tokens': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            }
        }
    