from rest_framework import generics, serializers
# from rest_framework import status
# from rest_framework.response import Response
from apps.identificationNFC.models import activeModel, identification
from apps.identificationNFC.api.serializers import ActiveModelSerializer, IdentificationSerializer, IdentificationUpdateSerializer

class ActiveModelListAPIView(generics.ListAPIView):
    serializer_class = ActiveModelSerializer

    def get_queryset(self):
        return activeModel.objects.all()

class IdentificationCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = IdentificationSerializer

    def get_queryset(self):
        return identification.objects.all()

class IdentificationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = identification.objects.all()
    serializer_class = IdentificationUpdateSerializer

    # def get_queryset(self):
    #     return self.get_serializer().Meta.model.objects.all()

    # def delete(self, request, pk=None):
    #     identification = self.get_queryset().filter(id=pk).first()
    #     if identification:
    #         identification.state = False
    #         identification.save()
    #         return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
    #     return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)}