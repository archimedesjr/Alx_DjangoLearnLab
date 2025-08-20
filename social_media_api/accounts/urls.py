from .views import CustomUserRegistrationView, UserProfileView
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("register/", CustomUserRegistrationView.as_view(), name="templates/registration/signup"),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path("follow/<int:user_id>/", views.follow_user, name="follow-user"),
    path("unfollow/<int:user_id>/", views.unfollow_user, name="unfollow-user"),
]