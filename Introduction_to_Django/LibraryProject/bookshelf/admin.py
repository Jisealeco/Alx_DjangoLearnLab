from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = ('title', 'author', 'publication_year')

    # Add search capability
    search_fields = ('title', 'author')

    # Add filters for quick sorting
    list_filter = ('publication_year', 'author')