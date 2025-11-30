from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from api.models import Author, Book


class BookAPITests(TestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Login required by checker
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

        # Create test data
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Python Basics",
            publication_year=2020,
            author=self.author
        )

    # ---------- List Books ----------
    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    # ---------- Create Book ----------
    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "New Book")

    # ---------- Retrieve Book ----------
    def test_retrieve_book(self):
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Python Basics")

    # ---------- Update Book ----------
    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.put(f"/api/books/update/{self.book.id}/", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Updated Book")

    # ---------- Delete Book ----------
    def test_delete_book(self):
        response = self.client.delete(f"/api/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    # ---------- Filtering ----------
    def test_filter_books_by_title(self):
        response = self.client.get("/api/books/?title=Python Basics")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    # ---------- Search ----------
    def test_search_books(self):
        response = self.client.get("/api/books/?search=John")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    # ---------- Ordering ----------
    def test_order_books(self):
        Book.objects.create(
            title="A Book",
            publication_year=1990,
            author=self.author
        )
        response = self.client.get("/api/books/?ordering=-publication_year")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 2)
