from django.test import TestCase
from django.urls import reverse
from ai_app.models import Book
# Zastąp 'ai_app' nazwą Twojej aplikacji
from datetime import datetime, timedelta


# Definiujemy klasę BookModelTest, która dziedziczy po TestCase,
# co oznacza, że jest to klasa testowa Django dla modeli.
class BookModelTest(TestCase):

    def setUp(self):
        # Metoda setUp ustawia warunki początkowe dla testów.
        # Tworzymy instancje książek do wykorzystania w testach.
        Book.objects.create(title="Test Book",
                            author="Author Name",
                            borrow_count=101,
                            published_date=datetime.now().date() - timedelta(days=30)
                            )
        Book.objects.create(title="Another Test Book",
                            author="Another Author",
                            borrow_count=50,
                            published_date=datetime.now().date() - timedelta(days=800)
                            )

    def test_is_popular(self):
        # Metoda test_is_popular sprawdza działanie metody is_popular modelu Book.
        # Pobieramy książki stworzone w metodzie setUp.
        popular_book = Book.objects.get(title="Test Book")
        not_popular_book = Book.objects.get(title="Another Test Book")

        # Używamy asercji, aby potwierdzić, czy książka jest uznawana za popularną.
        self.assertTrue(popular_book.is_popular())  # Sprawdzamy, czy popular_book jest popularna.
        self.assertFalse(not_popular_book.is_popular()) # Sprawdzamy, czy not_popular_book nie jest popularna.
    #
    # def test_book_creation(self):
    #     # Metoda test_book_creation sprawdza, czy książki są poprawnie tworzone.
    #     book = Book.objects.get(title="Test Book")
    #
    #     # Sprawdzamy, czy atrybuty książki są prawidłowo ustawione.
    #     self.assertEqual(book.author, "Author Name")  # Autor powinien być "Author Name".
    #     self.assertEqual(book.borrow_count, 101)  # Liczba wypożyczeń powinna wynosić 101.
    #
    # def test_genre(self):
    #     # Metoda test_genre sprawdza, czy pole genre można poprawnie zmodyfikować i zapisać.
    #     book = Book.objects.get(title="Test Book")
    #     book.genre = "Fantasy"  # Ustawiamy gatunek na "Fantasy".
    #     book.save()  # Zapisujemy zmianę w bazie danych.
    #     self.assertEqual(book.genre, "Fantasy")  # Sprawdzamy, czy gatunek został prawidłowo zaktualizowany.
    #
    # def test_string_representation(self):
    #     # Metoda test_string_representation sprawdza, czy metoda string_representation działa poprawnie.
    #     book = Book.objects.get(title="Test Book")
    #     self.assertEqual(book.string_representation(),
    #                      "Test Book by Author Name")  # Sprawdzamy reprezentację stringową książki.
    #
    # def test_get_absolute_url(self):
    #     # Metoda test_get_absolute_url sprawdza, czy metoda get_absolute_url generuje poprawny URL.
    #     book = Book.objects.get(title="Test Book")
    #     self.assertEqual(book.get_absolute_url(), reverse('book-detail', kwargs={
    #         'pk': book.pk}))  # Sprawdzamy, czy URL do szczegółów książki jest poprawny.
    #
    # def test_available_default(self):
    #     # Metoda test_available_default sprawdza, czy domyślna wartość pola available jest ustawiona na True.
    #     book = Book.objects.get(title="Test Book")
    #     self.assertTrue(book.available)  # Sprawdzamy, czy książka jest domyślnie dostępna.
    #
    # def test_reserve_method(self):
    #     # Metoda test_reserve_method sprawdza, czy metoda reserve zmienia dostępność książki na False.
    #     book = Book.objects.get(title="Test Book")
    #     book.reserve()  # Rezerwujemy książkę.
    #     self.assertFalse(book.available)  # Sprawdzamy, czy książka nie jest dostępna po rezerwacji.
    #
    # def test_is_new_release(self):
    #     # Metoda test_is_new_release sprawdza, czy metoda is_new_release poprawnie identyfikuje nowe wydania.
    #     new_release_book = Book.objects.get(title="Test Book")
    #     self.assertTrue(new_release_book.is_new_release())  # Sprawdzamy, czy książka jest nowym wydaniem.
    #     not_new_release_book = Book
