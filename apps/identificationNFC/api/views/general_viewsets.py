from rest_framework import generics, viewsets
from apps.identificationNFC.models import activeModel, identification
from apps.users.authentication_mixins import Authenication
from apps.identificationNFC.api.serializers import ActiveModelSerializer, IdentificationSerializer, IdentificationUpdateSerializer

class IdentificationViewSet(Authenication, viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action=='update':
            serializer_class = IdentificationUpdateSerializer
            return serializer_class
        else:
            serializer_class = IdentificationSerializer
            
            return  serializer_class
            
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    

class ActiveViewSet(viewsets.ModelViewSet):
    serializer_class = ActiveModelSerializer
    queryset = serializer_class.Meta.model.objects.all()