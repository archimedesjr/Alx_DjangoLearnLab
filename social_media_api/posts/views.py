from rest_framework import generics, viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']  # filter by author ID
    search_fields = ['title', 'content']  # search by title/content
    ordering_fields = ['created_at', 'updated_at']  # order by time


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # current user
        user = self.request.user
        # get all posts from users they follow
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
