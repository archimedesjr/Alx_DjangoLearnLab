from rest_framework import serializers
from .models import CustomUser
class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'bio', 'profile_picture', 'followers', 'username', 'email', 'password'] # include all the CustomUser fields

    def create(self, validated_data):
        # Remove password from validated data and hash it properly
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # hash password
        user.save()
        return user