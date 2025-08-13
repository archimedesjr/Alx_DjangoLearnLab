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

    # ListView
    path('/posts/', views.PostListView.as_view(), name='post-list'),

    # CreateView
    path('/posts/new/', views.PostCreateView.as_view(), name='post-create'),

    # DetailView
    path('/posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # UpdateView
    path('/posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    
    # DeleteView
    path('/posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
