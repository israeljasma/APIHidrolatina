from rest_framework import authentication, exceptions
from rest_framework.authentication import get_authorization_header

from apps.users.authentication import ExpiringTokenAuthentication

class Authenication(authentication.BaseAuthentication):
    user = None
    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None

            token_expired = ExpiringTokenAuthentication()
            user = token_expired.authenticate_credentials(token)

            if user != None:
                self.user = user
                return user

        return None

    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailed('No se han enviado las credenciales.')

        return (self.user, None)