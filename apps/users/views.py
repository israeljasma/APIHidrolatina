from django.contrib.auth import authenticate

from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.api.serializers import CustomTokenObtainPairSerializer, CustomUserSerializer

from apps.users.api.serializers import UserTokenSerializer
from apps.users.models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(username = username, password = password)

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Exitoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    serializer_class = CustomUserSerializer
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id)
        if user.exists():
            # token = RefreshToken.for_user(user.first())
            RefreshToken.for_user(user.first())
            RefreshToken(self.request.data.get('refresh')).blacklist()
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario'}, status=status.HTTP_400_BAD_REQUEST)


class LoginNFC(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # nfc = request.POST.get('nfc')
        nfc = request.data.get('nfc')
        if nfc is not None:
            userId = User.objects.filter(nfc__NFC=nfc).values_list('id', flat=True).first()
            print(userId)
            if userId is not None:
                userInstance = User.objects.get(id=userId)
                user_serializer = CustomUserSerializer(userInstance)
                return Response({
                    'token': str(RefreshToken.for_user(userInstance).access_token),
                    'refresh-token': str(RefreshToken.for_user(userInstance)),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Exitoso'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Dispositivo NFC incorrecto.'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No se detecto dispositivo NFC.'}, status = status.HTTP_400_BAD_REQUEST)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        userId = request.user.id
        userInstance = User.objects.get(id=userId)
        user_serializer = CustomUserSerializer(userInstance)
        print(user_serializer.data)
        return Response({
            # 'token': str(RefreshToken.for_user(userInstance).access_token),
            # 'refresh-token': str(RefreshToken.for_user(userInstance)), 
            'user': user_serializer.data
        }, status=status.HTTP_200_OK)

# class Login(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         login_serializer = self.serializer_class(data = request.data, context = {'request':request})
#         if login_serializer.is_valid():
#             user = login_serializer.validated_data['user']
#             if user.is_active:
#                 token, created = Token.objects.get_or_create(user = user)
#                 user_serializer = UserTokenSerializer(user)
#                 if created:
#                     return Response({
#                         'token': token.key,
#                         'user': user_serializer.data,
#                         'message': 'Inicio de Sesión Exitoso.'
#                         }, status.HTTP_201_CREATED)
#                 else:
#                     token.delete()
#                     token = Token.objects.create(user = user)
#                     return Response({
#                         'token': token.key,
#                         'user': user_serializer.data,
#                         'message': 'Inicio de Sesión Exitoso.'
#                         }, status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': 'Ese usuario no puede iniciar sesión.'}, status = status.HTTP_401_UNAUTHORIZED)
#             print(login_serializer.validated_data['username'])
#             print(login_serializer.validated_data['password'])
#         else:
#             return Response({'error': 'Nombre de usuario o contraseña incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)
#         return Response({'mensaje':'Holas desde response'}, status = status.HTTP_200_OK)

# class LoginNFC(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         nfc = request.POST.get('nfc')
#         if nfc is not None:
#             userId = User.objects.filter(nfc__NFC=nfc).values_list('id', flat=True).first()
#             if userId is not None:
#                 userInstance = User.objects.get(id=userId)
#                 token, created = Token.objects.get_or_create(user = userInstance)
#                 user_serializer = UserTokenSerializer(userInstance)
#                 if created:
#                     return Response({
#                         'token': token.key,
#                         'user': user_serializer.data,
#                         'message': 'Inicio de Sesión Exitoso.'
#                         }, status.HTTP_201_CREATED)
#                 else:
#                     token.delete()
#                     token = Token.objects.create(user = userInstance)
#                     return Response({
#                         'token': token.key,
#                         'user': user_serializer.data,
#                         'message': 'Inicio de Sesión Exitoso.'
#                         }, status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': 'Dispositivo NFC incorrecto.'}, status = status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'No se detecto dispositivo NFC.'}, status = status.HTTP_400_BAD_REQUEST)