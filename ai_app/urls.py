from django.urls import path
from .views import BookDetailView

# Lista `urlpatterns` definiuje wzorce URL dla aplikacji, przypisując konkretne ścieżki URL do widoków.
urlpatterns = [
    # Definicja pojedynczego wzorca URL:
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]