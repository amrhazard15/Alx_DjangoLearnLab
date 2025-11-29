from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# ====== Book Views ======
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only for all

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only for all

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

# ====== Author Views ======
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class AuthorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthorUpdateView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthorDeleteView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
