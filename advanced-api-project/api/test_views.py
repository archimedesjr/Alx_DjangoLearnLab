from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        self.author = Author.objects.create(name="John Doe")
        self.book1 = Book.objects.create(title="Book One", author=self.author, publication_year=2020)
        self.book1 = Book.objects.create(title="Book Two", author=self.author, publication_year=2021)

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book1.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book1.id])
     # Create
    def test_create_book(self):
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2022}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)


     # Read(List)
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Read(Detail)
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

     # Update
    def test_update_book(self):
        data = {"title": "Updated Title", "author": self.author.id, "publication_year": 2020}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")


    # Delete
    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())
    
    
    # Filtering
    def test_filter_books_by_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=2020")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    
    # Searching
    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=Book Two")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book Two")

    # Ordering
    def test_order_books_by_year(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.data[0]["title"], "Book Two")

    # Permission
    def test_unauthenticated_user_cannot_create_book(self):
        self.client.logout()
        data = {"title": "Unauthorized Book", "author": self.author.id, "publication_year": 2022}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)




