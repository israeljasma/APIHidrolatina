from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from apps.users.authentication_mixins import Authenication
from apps.actions.api.serializers import actionDetectionSerializers
from apps.users.models import User

class actionDetectionViewSet(viewsets.ModelViewSet):
    serializer_class = actionDetectionSerializers
    queryset = serializer_class.Meta.model.objects.all()
