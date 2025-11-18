# Create Book

```python
from bookshelf.models import Book

Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Expected Output: Book instance created successfully
```

