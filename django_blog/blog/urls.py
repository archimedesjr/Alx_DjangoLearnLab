from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # your custom views for registration and profile

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Logout page
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Registration page (custom view)
    path('register/', views.register, name='register'),

    # Profile page (custom view)
    path('profile/', views.profile, name='profile'),
]
