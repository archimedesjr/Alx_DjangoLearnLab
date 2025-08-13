from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # your custom views for registration and profile

urlpatterns = [
    # Login page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout page
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Registration page (custom view)
    path('register/', views.register, name='register'),

    # Profile page (custom view)
    path('profile/', views.profile, name='profile'),
]
