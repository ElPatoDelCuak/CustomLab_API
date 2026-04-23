from customlab_models.repositories.usuarioRepository import UsuarioRepository
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
import pyotp
import qrcode
import io
import base64

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
        payload['email'] = UsuarioService.normalize_email(payload.get('email'))

        if not payload.get('email'):
            return {
                'success': False,
                'message': 'El email es obligatorio'
            }
        
        email_duplicated = UsuarioRepository.getUsuarioByEmail(payload['email'])
        if email_duplicated and email_duplicated['id_usuario'] != idUsuario:
            return {
                'success': False,
                'message': 'El email ya esta registrado'
            }

        try:
            payload['password'] = UsuarioService.validate_and_hash_password(payload.get('password'))
        except ValidationError as exc:
            return {
                'success': False,
                'message': '; '.join(exc.messages)
            }

        success = UsuarioRepository.updateUsuario(idUsuario, payload)
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

        # Verificar 2FA si está habilitado
        if usuario.get('doble_factor'):
            code_2fa = data.get('code_2fa')
            if not code_2fa:
                return {
                    'success': False,
                    'message': 'Código 2FA requerido'
                }
            if not UsuarioService.verify_2fa_code(usuario.get('secret_2fa'), code_2fa):
                return {
                    'success': False,
                    'message': 'Código 2FA inválido'
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

    @staticmethod
    def generate_2fa_secret():
        """Genera un secret para 2FA."""
        return pyotp.random_base32()

    @staticmethod
    def get_2fa_qr_code(email, secret):
        """Genera un QR code para configurar 2FA."""
        totp = pyotp.TOTP(secret)
        uri = totp.provisioning_uri(name=email, issuer_name="CustomLab API")
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(uri)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return f"data:image/png;base64,{img_str}"

    @staticmethod
    def enable_2fa(user_id, secret):
        """Habilita 2FA para un usuario."""
        return UsuarioRepository.updateUsuario(user_id, {'doble_factor': True, 'secret_2fa': secret})

    @staticmethod
    def disable_2fa(user_id):
        """Deshabilita 2FA para un usuario."""
        return UsuarioRepository.updateUsuario(user_id, {'doble_factor': False, 'secret_2fa': None})

    @staticmethod
    def verify_2fa_code(secret, code):
        """Verifica un código 2FA."""
        totp = pyotp.TOTP(secret)
        return totp.verify(code)
    