from django.views.generic.detail import DetailView
from .models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'ai_app/book_detail.html'  # Określ ścieżkę do swojego szablonu
    context_object_name = 'book'
