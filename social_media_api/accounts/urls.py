

from django.contrib.auth.views import LoginView, CustomUserRegistrationView, UserProfileView
from django.urls import path, include

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("register/", CustomUserRegistrationView.as_view(), name="templates/registration/signup"),
    path('profile/', UserProfileView.as_view(), name='profile'),
]