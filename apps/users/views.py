from datetime import datetime
import re

from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.api.serializers import UserTokenSerializer

class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(user = UserTokenSerializer().Meta.model.objects.filter(username = username).first())
            return Response({'token': user_token.key})
        except:
            return Response({'error': 'Credenciales enviadas incorrectas.'}, status = status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                        }, status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso.'
                        }, status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Ese usuario no puede iniciar sesión.'}, status = status.HTTP_401_UNAUTHORIZED)
            print(login_serializer.validated_data['username'])
            print(login_serializer.validated_data['password'])
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Holas desde response'}, status = status.HTTP_200_OK)


class Logout(APIView):

    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            print(token)
            token = Token.objects.filter(key = token).first()
            print(token)
            if token:
                user = token.user
                print(user)
                all_sessions  = Session.objects.filter(expire_date__gte=datetime.datetime.now())
                print(all_sessions)
                if all_sessions.exists():
                    print('llega?')
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                
                token.delete()

                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'

                return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK)

            return Response({'error': 'No se ha encontrado un usuario con estas credenciales.'}, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Nose ha encontrado token en la petición.'}, status = status.HTTP_409_CONFLICT)