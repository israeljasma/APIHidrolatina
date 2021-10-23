from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from apps.identificationNFC.models import activeModel, identification

class ActiveModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = activeModel
        fields = '__all__'

class IdentificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = identification
        fields = '__all__'
