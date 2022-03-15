from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User

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

class UserPPESerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'last_name')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        #Modelo
        model = User
        #campos a usar
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        #Modelo
        model = User
        #campos a usar
        fields = ('username', 'email', 'name', 'last_name')

    # def update(self, instance, validated_data):
    #     update_user = super().update(instance, validated_data)
    #     update_user.set_password(validated_data['password'])
    #     update_user.save()
    #     return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password','groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser')
        # fields = '__all__'