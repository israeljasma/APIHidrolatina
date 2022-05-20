from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.users.models import User
from apps.users.api.serializers import UpdateUserWithNfcSerializer, UserListSerializer, UserSerializer, UpdateUserSerializer, UserNFCSerializer, GroupSerializer

class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)
        # return self.serializer_class().Meta.model.objects.filter(id=pk).first()

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(is_active=True)
        return self.queryset
        
    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario registrado Correctamente.'}, status = status.HTTP_201_CREATED)
        return Response({'message': 'Hay errores en el registro.', 'errors': user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        if "nfc" in request.data:
            user_serializer = UpdateUserWithNfcSerializer(user, data=request.data)
        else:
            user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario actualizado correctamente.'}, status = status.HTTP_201_CREATED)
        return Response({'message':'Hay errores en la actualización.', 'errors':user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({'message':'Usuario eliminado Correctamente.'}, status = status.HTTP_201_CREATED)
        return Response({'message':'No existe el usuario que desea eliminar.'}, status = status.HTTP_404_NOT_FOUND)


class UserNFCViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    serializer_class = UserNFCSerializer
    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario registrado Correctamente.'}, status = status.HTTP_201_CREATED)
        return Response({'message': 'Hay errores en el registro.', 'errors': user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = serializer_class.Meta.model.objects.all()

# @api_view(['GET', 'POST'])
# def user_api_view(request):

#     # list
#     if request.method == 'GET':
#         # queryset
#         users = User.objects.all()
#         users_serializer = UserListSerializer(users, many = True)

#         return Response(users_serializer.data, status = status.HTTP_200_OK)

#     # create
#     elif request.method == 'POST':
#         users_serializer = CustomUserSerializer(data = request.data)

#         # validation
#         if users_serializer.is_valid():
#             users_serializer.save()
#             return Response({'message':'Usuario creado Correctamente!'}, status = status.HTTP_201_CREATED)

#         return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail_api_view(request, pk = None):
#     # queryset
#     user = User.objects.filter(id = pk).first()

#     # validation
#     if user:

#         # retrieve
#         if request.method == 'GET':
#             user_serializer = CustomUserSerializer(user)
#             return Response(user_serializer.data, status = status.HTTP_200_OK)
        
#         # update
#         elif request.method == 'PUT':
#             user_serializer = CustomUserSerializer(user, data = request.data)
#             if user_serializer.is_valid():
#                 user_serializer.save()
#                 return Response({'message':'Usuario modificado Correctamente!'}, status = status.HTTP_200_OK)
#             return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
#         # delete
#         elif request.method == 'DELETE':
#             user.delete()
#             return Response({'message':'Usuario Eliminado correctamente!'}, status = status.HTTP_200_OK)
#     return Response({'message':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
