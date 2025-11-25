from django.shortcuts import render

# Create your views here.
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # available in template as 'library'

    # Optional if you want to fetch object manually
    def get_object(self, queryset=None):
        library_id = self.kwargs.get('pk')
        return get_object_or_404(Library, pk=library_id)