from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from django.utils.translation import gettext_lazy as _
from customlab_models.models import Usuarios

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        It uses the 'id_usuario' claim from the token to find the user in the custom 'Usuarios' model.
        """
        try:
            user_id = validated_token.get('id_usuario') or validated_token.get('user_id')
            if not user_id:
                raise KeyError
        except KeyError:
            raise InvalidToken(_("Token contained no recognizable user identification"))

        try:
            user = Usuarios.objects.get(id_usuario=user_id)
        except Usuarios.DoesNotExist:
            raise AuthenticationFailed(_("User not found"), code="user_not_found")
            
        # Add is_authenticated attribute so that DRF's IsAuthenticated permission works
        user.is_authenticated = True
        return user
