from apps.sensors.models import FeedConductivity, FeedTemperature, MembranePermeateFlow, MembraneRejectionFlow, MembraneFeedPressure, MembraneRejectionPressure, ConductivityPermeateMembranes, VesselsPermeateFlow, VesselsFeedingFlow, FeedPressureVessels, RejectPressureVessels, ConductivityPermeateVessels, RegisterMembranes, RegisterVessels

from rest_framework import serializers

class FeedConductivitySerializers(serializers.ModelSerializer):

    class Meta:
        model = FeedConductivity
        fields = '__all__'


class FeedTemperatureSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = FeedTemperature
        fields = '__all__'


class MembranePermeateFlowSerializers(serializers.ModelSerializer):

    class Meta:
        model = MembranePermeateFlow
        fields = '__all__'


class MembraneRejectionFlowSerializers(serializers.ModelSerializer):

    class Meta:
        model = MembraneRejectionFlow
        fields = '__all__'


class MembraneFeedPressureSerializers(serializers.ModelSerializer):

    class Meta:
        model = MembraneFeedPressure
        fields = '__all__'


class MembraneRejectionPressureSerializers(serializers.ModelSerializer):

    class Meta:
        model = MembraneRejectionPressure
        fields = '__all__'


class ConductivityPermeateMembranesSerializers(serializers.ModelSerializer):

    class Meta:
        model = ConductivityPermeateMembranes
        fields = '__all__'

class VesselsPermeateFlowSerializers(serializers.ModelSerializer):

    class Meta:
        model = VesselsPermeateFlow
        fields = '__all__'

class VesselsFeedingFlowSerializers(serializers.ModelSerializer):

    class Meta:
        model = VesselsFeedingFlow
        fields = '__all__'

class FeedPressureVesselsSerializers(serializers.ModelSerializer):

    class Meta:
        model = FeedPressureVessels
        fields = '__all__'

class RejectPressureVesselsSerializers(serializers.ModelSerializer):

    class Meta:
        model = RejectPressureVessels
        fields = '__all__'

class ConductivityPermeateVesselsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ConductivityPermeateVessels
        fields = '__all__'

class RegisterMembranesSerializers(serializers.ModelSerializer):

    class Meta:
        model = RegisterMembranes
        fields = '__all__'

class RegisterVesselsSerializers(serializers.ModelSerializer):

    class Meta:
        model = RegisterVessels
        fields = '__all__'