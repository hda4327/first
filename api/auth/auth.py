from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from api.models import *


class Authentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.query_params.get("token")
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("验证失败!")
        return token_obj.username, token_obj
