from rest_framework import serializers
from .models import Author, Book
from datetime import datetime
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Validates that publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']