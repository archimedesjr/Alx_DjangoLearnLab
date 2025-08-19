from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ explicit CharField

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']

    def create(self, validated_data):
        password = validated_data.pop('password')
        # ✅ use create_user instead of manually instantiating
        user = get_user_model().objects.create_user(password=password, **validated_data)
        Token.objects.create(user=user)  # optional: give token immediately
        return user
