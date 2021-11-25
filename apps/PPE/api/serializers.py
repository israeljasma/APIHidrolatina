from apps.PPE.models import detectionPPE

from rest_framework import serializers

class detectionPPESerializers(serializers.ModelSerializer):

    class Meta:
        model = detectionPPE
        exclude = ('state',)