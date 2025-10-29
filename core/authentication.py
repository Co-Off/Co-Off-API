from django.contrib.auth import authenticate
from rest_framework import authentication, exceptions
from core.models import User


class TokenAuthentication(authentication.BaseAuthentication):
    """
    Autenticação local simples baseada em token (pode ser adaptada para JWT depois).
    Espera o header:
        Authorization: Token <username>:<password>
    Exemplo:
        Authorization: Token daniel:12345
    """

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Token "):
            return None

        try:
            credentials = auth_header.split("Token ")[1]
            username, password = credentials.split(":")
        except ValueError:
            raise exceptions.AuthenticationFailed("Formato inválido de token.")

        user = authenticate(username=username, password=password)
        if user is None:
            raise exceptions.AuthenticationFailed("Credenciais inválidas.")

        return (user, None)
