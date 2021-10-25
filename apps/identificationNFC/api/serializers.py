from django.db.models import fields
from django.db.models.base import Model
from django.db.models.query import QuerySet
from rest_framework import serializers
from apps.identificationNFC.models import activeModel, identification

class ActiveModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = activeModel
        fields = '__all__'

class IdentificationSerializer(serializers.ModelSerializer):
    active = serializers.PrimaryKeyRelatedField(queryset= activeModel.objects.filter(active=True))
    # active = ActiveModelSerializer()
    class Meta:
        model = identification
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     return {
    #         'id': instance.id,
    #         'active' : instance.active,
    #         # 'description' : instance.description,
    #         # 'created_date' : instance.created_date,
    #         # 'modified_date' : instance.modified_date
    #     }

class IdentificationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = identification
        fields = '__all__'
