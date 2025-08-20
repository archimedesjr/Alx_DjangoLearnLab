from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer, UserSerializer

class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Always return the logged-in user
        return self.request.user
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def follow_user(self, request, pk=None):
        """Allow the current user to follow another user"""
        user_to_follow = self.get_object()
        current_user = request.user

        if user_to_follow == current_user:
            return Response({"detail": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        current_user.following.add(user_to_follow)
        user_to_follow.followers.add(current_user)  # keep both in sync

        return Response({"detail": f"You are now following {user_to_follow.username}."})

    @action(detail=True, methods=["post"])
    def unfollow_user(self, request, pk=None):
        """Allow the current user to unfollow another user"""
        user_to_unfollow = self.get_object()
        current_user = request.user

        if user_to_unfollow == current_user:
            return Response({"detail": "You cannot unfollow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)

        current_user.following.remove(user_to_unfollow)
        user_to_unfollow.followers.remove(current_user)  # keep both in sync

        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."})