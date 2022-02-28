from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.identificationNFC.api.serializers import ActiveModelSerializer, IdentificationSerializer, IdentificationUpdateSerializer

class IdentificationViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action=='update':
            serializer_class = IdentificationUpdateSerializer
            return serializer_class
        else:
            serializer_class = IdentificationSerializer
            return serializer_class
            
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def create(self, request, *args, **kwargs):
        nfc_serializer = IdentificationSerializer(data=request.data)
        if nfc_serializer.is_valid():
            nfc_serializer.save()
            return Response({'message': 'NFC Yeey', 'data': nfc_serializer.data},status=status.HTTP_200_OK)
        return Response({'message': 'Hay errores en el registro.', 'errors': nfc_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        if IdentificationSerializer.Meta.model.objects.filter(pk=pk):
            nfc = IdentificationSerializer.Meta.model.objects.filter(pk=pk).update(state=False)
            return Response({'message': 'NFC eliminado correctamente.'},status=status.HTTP_200_OK)
        return Response({'message': 'NFC no encontrado'},status=status.HTTP_404_NOT_FOUND)

class ActiveViewSet(viewsets.ModelViewSet):
    serializer_class = ActiveModelSerializer
    queryset = serializer_class.Meta.model.objects.all()