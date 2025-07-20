from django.urls import path
from .views import LibraryDetailView

urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
]
