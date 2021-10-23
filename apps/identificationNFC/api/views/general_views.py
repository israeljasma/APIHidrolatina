from rest_framework import generics, serializers
from apps.identificationNFC.models import activeModel, identification
from apps.identificationNFC.api.serializers import ActiveModelSerializer, IdentificationSerializer

class ActiveModelListAPIView(generics.ListAPIView):
    serializer_class = ActiveModelSerializer

    def get_queryset(self):
        return activeModel.objects.all()

class IdentificationSerializerListAPIView(generics.ListAPIView):
    serializer_class = IdentificationSerializer

    def get_queryset(self):
        return identification.objects.all()