from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import LibraryDetailView
from .views import list_books
from relationship_app import views

urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

]
