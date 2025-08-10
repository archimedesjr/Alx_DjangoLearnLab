from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book 
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer

# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Using the DjangoFilterBackend saved us the stress of writing the commented get_queryset method
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] # ✅ Enables filtering
    # ✅ Fields the API can filter on
    filterset_fields = ['author__name', 'publication_year', 'title']
    search_fields = ['author__name', 'title']
    ordering_fields = ['publication_year', 'title']
    # def get_queryset(self):
    #     queryset = Book.objects.all()
        
    #     #Get query parameters 
    #     author_name = self.request.query_params.get('author')
    #     title  = self.request.query_params.get('title')
    #     year = self.request.query_params.get('published_year')

    #     #Filter by author name if provided
    #     if author_name:
    #         queryset = queryset.filter(author__name__icontains=author_name)

    #     #Filter by title name if provided
    #     if title:
    #         queryset = queryset.filter(title=title)

    #     # Filter by published year if provided
    #     if year:
    #         queryset = queryset.filter(publication_year=year)

    #     return queryset


# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ only logged-in users can create


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ only creators can update

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]