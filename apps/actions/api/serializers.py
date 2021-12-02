from apps.actions.models import actionDetection

from rest_framework import serializers

class actionDetectionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = actionDetection
        exclude = ('state',)