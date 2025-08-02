from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookList(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer