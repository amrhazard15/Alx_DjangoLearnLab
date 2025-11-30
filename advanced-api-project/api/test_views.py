from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITests(APITestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(username="amr", password="123456")

        # Client for authenticated requests
        self.auth_client = APIClient()
        self.auth_client.login(username="amr", password="123456")
        self.client.login(username="testuser", password="testpassword")

        # Create authors
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Mark Smith")

        # Create books
        self.book1 = Book.objects.create(
            title="Python Basics",
            author=self.author1,
            publication_year=2020
        )

        self.book2 = Book.objects.create(
            title="Advanced Django",
            author=self.author2,
            publication_year=2022
        )

    # =========================
    #        LIST VIEW
    # =========================
    def test_get_book_list(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # =========================
    #        DETAIL VIEW
    # =========================
    def test_get_book_detail(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Python Basics")

    # =========================
    #        CREATE
    # =========================
    def test_create_book_authenticated(self):
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2023
        }
        response = self.auth_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2023
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # =========================
    #        UPDATE
    # =========================
    def test_update_book(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Title", "author": self.author1.id, "publication_year": 2021}

        response = self.auth_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # =========================
    #        DELETE
    # =========================
    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book1.id])
        response = self.auth_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # =========================
    #   Filtering
    # =========================
    def test_filter_books_by_title(self):
        url = reverse("book-list") + "?title=Python Basics"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

    # =========================
    #   Search
    # =========================
    def test_search_books(self):
        url = reverse("book-list") + "?search=Python"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

    # =========================
    #   Ordering
    # =========================
    def test_ordering_books(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.data[0]["publication_year"], 2022)

