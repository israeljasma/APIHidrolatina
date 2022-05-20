from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.identificationNFC.api.serializers import IdentificationSerializer
from apps.identificationNFC.models import identification

from apps.users.models import User
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

class UserCustomRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'last_name')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        #Modelo
        model = User
        #campos a usar
        exclude = ('user_permissions', 'is_active', 'is_staff', 'is_superuser', 'last_login')
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserNFCSerializer(serializers.ModelSerializer):

    nfc = IdentificationSerializer(many=True)

    class Meta:
        #Modelo
        model = User
        #campos a usar
        exclude = ('user_permissions', 'is_active', 'is_staff', 'is_superuser', 'last_login')
    
    def create(self, validated_data):
        nfcs_data = validated_data.pop('nfc')
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        for nfc_data in nfcs_data:
            identification.objects.create(user = user, **nfc_data)
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        #Modelo
        model = User
        #campos a usar
        fields = ('username', 'email', 'name', 'last_name')

class UpdateUserWithNfcSerializer(serializers.ModelSerializer):
    class Meta:
        #Modelo
        model = User
        #campos a usar
        fields = ('username', 'email', 'name', 'last_name', 'nfc')

    # def update(self, instance, validated_data):
    #     update_user = super().update(instance, validated_data)
    #     update_user.set_password(validated_data['password'])
    #     update_user.save()
    #     return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'user_permissions', 'is_active', 'is_staff', 'is_superuser')
        # fields = '__all__'

