from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField() # ✅ explicit CharField

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']

    def create(self, validated_data):
        password = validated_data.pop('password')
        # ✅ use create_user instead of manually instantiating
        user = get_user_model().objects.create_user(password=password, **validated_data)
        Token.objects.create(user=user)  # optional: give token immediately
        return user
    
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source="followers.count", read_only=True)
    following_count = serializers.IntegerField(source="following.count", read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "followers_count", "following_count"]
