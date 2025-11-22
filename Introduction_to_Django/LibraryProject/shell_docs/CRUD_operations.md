## create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

##Expected output:
Book: 1984 by George Orwell>

## Retrieve
book = Book.objects.get(id=1)
book

##Expected output:
Book: 1984 by George Orwell

##Update
book.title = "Nineteen Eighty-Four"
book.save()
book

##Expected output:
Book: Nineteen Eighty-Four by George Orwell

##Delete
book.delete()
Book.objects.all()

##Expected output:
(1, {'bookshelf.Book': 1})
QuerySet []