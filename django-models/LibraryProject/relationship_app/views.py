from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'books/list_book.html', context)

class LibraryDetailView(DetailView):
  """A class-based view for displaying details of a specific Library."""
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the Library."""
    context = super().get_context_data(**kwargs)  # Get default context data
    context['books'] = self.object.books.all()
    return context