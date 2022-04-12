from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from apps.users.authentication_mixins import Authenication
from apps.PPE.api.serializers import detectionPPESerializers, detectionPPERepresentationSerializers
from apps.users.models import User

class detectionPPEViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action=='list':
            serializer_class = detectionPPERepresentationSerializers
            return serializer_class
        else:
            serializer_class = detectionPPESerializers
            return serializer_class

    def get_queryset(self):
        if (self.request.GET.get('user')):
            print(self.request.GET["user"])
            return self.get_serializer().Meta.model.objects.filter(user=self.request.GET["user"]).order_by('-date')
        else:
            return self.get_serializer().Meta.model.objects.all().order_by('-date')
    # serializer_class = detectionPPERepresentationSerializers
    # queryset = serializer_class.Meta.model.objects.all()
    

    def perform_create(self, serializer):
        user_id = self.request.user.id
        userInstance = User.objects.get(id=user_id)
        serializer.save(user=userInstance)

