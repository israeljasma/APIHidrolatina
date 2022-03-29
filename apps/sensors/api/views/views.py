from rest_framework import viewsets

from apps.users.authentication_mixins import Authenication
from apps.sensors.api.serializers import FeedConductivitySerializers, FeedTemperatureSerializers, MembranePermeateFlowSerializers, MembraneRejectionFlowSerializers, MembraneFeedPressureSerializers, MembraneRejectionPressureSerializers, ConductivityPermeateMembranesSerializers, VesselsPermeateFlowSerializers, VesselsFeedingFlowSerializers, FeedPressureVesselsSerializers, RejectPressureVesselsSerializers, ConductivityPermeateVesselsSerializers, RegisterMembranesSerializers, RegisterVesselsSerializers


class FeedConductivityViewSet(viewsets.ModelViewSet):
    serializer_class = FeedConductivitySerializers
    queryset = serializer_class.Meta.model.objects.all()

class FeedTemperatureViewSet(viewsets.ModelViewSet):
    serializer_class = FeedTemperatureSerializers
    queryset = serializer_class.Meta.model.objects.all()

class MembranePermeateViewSet(viewsets.ModelViewSet):
    serializer_class = MembranePermeateFlowSerializers
    queryset = serializer_class.Meta.model.objects.all()

class MembraneRejectionFlowViewSet(viewsets.ModelViewSet):
    serializer_class = MembraneRejectionFlowSerializers
    queryset = serializer_class.Meta.model.objects.all()

class MembraneFeedPressureViewSet(viewsets.ModelViewSet):
    serializer_class = MembraneFeedPressureSerializers
    queryset = serializer_class.Meta.model.objects.all()

class MembraneRejectionPressureViewSet(viewsets.ModelViewSet):
    serializer_class = MembraneRejectionPressureSerializers
    queryset = serializer_class.Meta.model.objects.all()

class ConductivityPermeateMembranesViewSet(viewsets.ModelViewSet):
    serializer_class = ConductivityPermeateMembranesSerializers
    queryset = serializer_class.Meta.model.objects.all()

class VesselsPermeateFlowViewSet(viewsets.ModelViewSet):
    serializer_class = VesselsPermeateFlowSerializers
    queryset = serializer_class.Meta.model.objects.all()

class VesselsFeedingFlowViewSet(viewsets.ModelViewSet):
    serializer_class = VesselsFeedingFlowSerializers
    queryset = serializer_class.Meta.model.objects.all()

class FeedPressureVesselsViewSet(viewsets.ModelViewSet):
    serializer_class = FeedPressureVesselsSerializers
    queryset = serializer_class.Meta.model.objects.all()

class RejectPressureVesselsViewSet(viewsets.ModelViewSet):
    serializer_class = RejectPressureVesselsSerializers
    queryset = serializer_class.Meta.model.objects.all()

class ConductivityPermeateVesselsViewSet(viewsets.ModelViewSet):
    serializer_class = ConductivityPermeateVesselsSerializers
    queryset = serializer_class.Meta.model.objects.all()

class RegisterMembranesViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterMembranesSerializers
    queryset = serializer_class.Meta.model.objects.all()

class RegisterVesselsViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterVesselsSerializers
    queryset = serializer_class.Meta.model.objects.all()