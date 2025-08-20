from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet, FeedView

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("feed/", FeedView.as_view(), name="user-feed"),
]