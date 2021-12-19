from rest_framework import viewsets

from apps.users.authentication_mixins import Authenication
from apps.sensors.models import RejectFlow
from apps.sensors.api.serializers import RejectFlowSerializers, PermeateFlowSerializers, PermeateConductivitySerializers, RejectionPressureSerializers, FeedConductivitySerializers, DeedingTemperatureSerializers, FeedPressureSerializers

class RejectFlowViewSet(viewsets.ModelViewSet):
    serializer_class = RejectFlowSerializers
    queryset = serializer_class.Meta.model.objects.all()

class PermeateFlowViewSet(viewsets.ModelViewSet):
    serializer_class = PermeateFlowSerializers
    queryset = serializer_class.Meta.model.objects.all()

class PermeateConductivityViewSet(viewsets.ModelViewSet):
    serializer_class = PermeateConductivitySerializers
    queryset = serializer_class.Meta.model.objects.all()

class RejectionPressureViewSet(viewsets.ModelViewSet):
    serializer_class = RejectionPressureSerializers
    queryset = serializer_class.Meta.model.objects.all()

class FeedConductivityViewSet(viewsets.ModelViewSet):
    serializer_class = FeedConductivitySerializers
    queryset = serializer_class.Meta.model.objects.all()

class DeedingTemperatureViewSet(viewsets.ModelViewSet):
    serializer_class = DeedingTemperatureSerializers
    queryset = serializer_class.Meta.model.objects.all()

class FeedPressureViewSet(viewsets.ModelViewSet):
    serializer_class = FeedPressureSerializers
    queryset = serializer_class.Meta.model.objects.all()