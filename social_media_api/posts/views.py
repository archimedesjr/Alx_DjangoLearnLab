from rest_framework import generics, viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, Post, Like, Notification
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

class LikePostView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, id=post_id)

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create notification (don’t notify self-likes)
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target_post=post
                )
            return JsonResponse({"status": "liked"})
        else:
            return JsonResponse({"status": "already_liked"})

class UnlikePostView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = generics.get_object_or_404(Post, id=post_id)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return JsonResponse({"status": "unliked"})
        return JsonResponse({"status": "not_liked"})
