```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book

Output
Book: 1984 by George Orwell