from pyexpat import model
from apps.actions.models import actionDetection, risk, action

from rest_framework import serializers

from apps.users.api.serializers import UserCustomRepresentationSerializer

class actionSerializers(serializers.ModelSerializer):

    class Meta:
        model = action
        fields = ('id', 'action')

class riskSerializers(serializers.ModelSerializer):

    class Meta:
        model = risk
        fields = ('id', 'risk')

class actionDetectionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = actionDetection
        exclude = ('state',)

class actionDetectionRepresentationSerializers(serializers.ModelSerializer):

    user = UserCustomRepresentationSerializer(read_only=True)
    risk = riskSerializers(read_only=True)
    action = actionSerializers(read_only=True)
    
    class Meta:
        model = actionDetection
        fields = ('id', 'operator_present', 'action', 'risk', 'hour', 'date', 'user', 'created_date', 'modified_date')
        # exclude = ('state',)