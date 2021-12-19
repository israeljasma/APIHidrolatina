from apps.sensors.models import RejectFlow, PermeateFlow, PermeateConductivity, RejectionPressure, FeedConductivity, DeedingTemperature, FeedPressure

from rest_framework import serializers

class RejectFlowSerializers(serializers.ModelSerializer):

    class Meta:
        model = RejectFlow
        fields = '__all__'


class PermeateFlowSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = PermeateFlow
        fields = '__all__'


class PermeateConductivitySerializers(serializers.ModelSerializer):

    class Meta:
        model = PermeateConductivity
        fields = '__all__'


class RejectionPressureSerializers(serializers.ModelSerializer):

    class Meta:
        model = RejectionPressure
        fields = '__all__'


class FeedConductivitySerializers(serializers.ModelSerializer):

    class Meta:
        model = FeedConductivity
        fields = '__all__'


class DeedingTemperatureSerializers(serializers.ModelSerializer):

    class Meta:
        model = DeedingTemperature
        fields = '__all__'


class FeedPressureSerializers(serializers.ModelSerializer):

    class Meta:
        model = FeedPressure
        fields = '__all__'