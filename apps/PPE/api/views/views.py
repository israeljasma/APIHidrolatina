from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from apps.users.authentication_mixins import Authenication
from apps.PPE.api.serializers import detectionPPESerializers
from apps.users.models import User

class detectionPPEViewSet(viewsets.ModelViewSet):
    serializer_class = detectionPPESerializers
    queryset = serializer_class.Meta.model.objects.all()

    def perform_create(self, serializer):
        print(self.request.data)
        user_id = Token.objects.get(key=self.request.data['token']).user_id
        userInstance = User.objects.get(id=user_id)
        serializer.save(user=userInstance)


