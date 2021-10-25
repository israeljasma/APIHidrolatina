from django.db.models import query
from rest_framework import generics
# from rest_framework import status
# from rest_framework.response import Response
from apps.identificationNFC.models import activeModel, identification
from apps.identificationNFC.api.serializers import ActiveModelSerializer, IdentificationSerializer, IdentificationUpdateSerializer

class ActiveModelListAPIView(generics.ListAPIView):
    serializer_class = ActiveModelSerializer

    def get_queryset(self):
        return activeModel.objects.all()

class IdentificationSerializerListAPIView(generics.ListAPIView):
    serializer_class = IdentificationSerializer

    def get_queryset(self):
        return identification.objects.all()

class IdentificationCreateAPIView(generics.CreateAPIView):
    serializer_class = IdentificationSerializer

class IdentificationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = identification.objects.all()
    serializer_class = IdentificationSerializer

    # def get_queryset(self):
    #     return self.get_serializer().Meta.model.objects.all()

class IdentificationDestroyAPIView(generics.DestroyAPIView):
    queryset = identification.objects.all()
    serializer_class = IdentificationSerializer

    # def delete(self, request, pk=None):
    #     identification = self.get_queryset().filter(id=pk).first()
    #     if identification:
    #         identification.state = False
    #         identification.save()
    #         return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
    #     return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)}

class IdentificationUpdateAPIView(generics.UpdateAPIView):
    queryset = identification.objects.all()
    serializer_class = IdentificationUpdateSerializer