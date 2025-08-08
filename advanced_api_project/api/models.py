from django.db import models

# Create your models here.
# Author model: represents a book author
class Author(models.Model):
    name = models.CharField(max_length=200)

# Book model: represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.IntegerField()
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books' # allows reverse lookup like author.books.all()
    )