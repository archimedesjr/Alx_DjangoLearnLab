from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("feed/", FeedView.as_view(), name="user-feed"),
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="like_post"),
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike_post"),
]