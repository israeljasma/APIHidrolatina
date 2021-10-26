from rest_framework import generics, viewsets
from apps.identificationNFC.api.serializers import ActiveModelSerializer, IdentificationSerializer, IdentificationUpdateSerializer

class IdentificationViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action=='update':
            serializer_class = IdentificationUpdateSerializer
            return serializer_class
        else:
            serializer_class = IdentificationSerializer
            return  serializer_class


class ActiveViewSet(generics.ListAPIView):
    serializer_class = ActiveModelSerializer