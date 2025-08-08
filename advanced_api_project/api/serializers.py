from rest_framework import serializers
from .models import Book, Author
import datetime

# BookSerializer: handles serialization of the Book model
class BookSerializer(serializers.ModelSerializer):

# Custom validation to ensure the year is not in the future
    def validate(self, data):
        current_year = datetime.date.today().year
        if data['published_year'] > current_year:
            raise serializers.ValidationError("Publication Year cannot be in future.")
        return data
    
    class Meta:
        model = Book
        fields = ['title','published_year', 'author'] # include all fields

# AuthorSerializer: serializes the Author model and nests BookSerializer for related books
class AuthorSerializer(serializers.ModelSerializer):
    # Use the related_name "books" to nest the serialized book objects
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name']
