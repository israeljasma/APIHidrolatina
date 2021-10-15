from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        #Modelo
        model = User
        #campos a usar
        fields = '__all__'