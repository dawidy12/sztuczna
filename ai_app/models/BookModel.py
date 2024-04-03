# Importujemy moduł models z Django, który zawiera definicje pól modelu i innych funkcji ORM.
from django.db import models
# Importujemy funkcję reverse, która jest używana do odwracania wzorców URL
# i generowania URL-ów na podstawie nazw wzorców.
from django.urls import reverse
# Importujemy moduły datetime i timedelta do manipulowania datami i czasem.
from datetime import datetime, timedelta
# Importujemy moduł date, aby uzyskać obiekt daty dzisiejszej.
from datetime import date


# Definiujemy klasę Book, która dziedziczy po models.Model, oznaczając, że jest to model Django.
class Book(models.Model):
    # Definiujemy pola modelu:
    # Pole tekstowe dla tytułu książki, które może zawierać maksymalnie 100 znaków.
    title = models.CharField(max_length=100)
    # Podobne pole tekstowe dla autora książki.
    author = models.CharField(max_length=100)
    # Pole tekstowe dla gatunku literackiego, które może być puste (blank=True).
    genre = models.CharField(max_length=100, blank=True)
    # Liczbowe pole całkowite dla liczby wypożyczeń z domyślną wartością 0.
    borrow_count = models.IntegerField(default=0)
    # Pole daty publikacji z domyślną wartością dzisiejszej daty.
    published_date = models.DateField(default=date.today)
    # Pole logiczne, które wskazuje, czy książka jest dostępna, domyślnie ustawione na True.
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # Definiujemy metody instancji modelu:
    def is_popular(self):
        """Zwraca True, jeśli książka została wypożyczona więcej niż 100 razy."""
        # Zwraca wartość logiczną True, jeśli liczba wypożyczeń przekracza 100.
        return self.borrow_count > 100

    def is_new_release(self):
        """Sprawdza, czy książka jest nowym wydaniem (wydana w ciągu ostatnich 2 lat)."""
        # Zwraca True, jeśli książka została wydana w ciągu ostatnich dwóch lat.
        return (datetime.now().date() - self.published_date) <= timedelta(days=730)

    def string_representation(self):
        """Zwraca reprezentację stringową książki."""
        # Formatuje i zwraca tytuł i autora książki jako string.
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        """Generuje URL do szczegółów książki."""
        # Używa funkcji reverse do wygenerowania URL na podstawie nazwy wzorca URL 'book-detail'
        # i klucza głównego (pk) książki.
        return reverse('book-detail', kwargs={'pk': self.pk})

    def reserve(self):
        """Rezerwuje książkę (zmienia dostępność na False)."""
        # Ustawia atrybut available na False, oznaczając, że książka jest zarezerwowana.
        self.available = False
        # Zapisuje zmianę stanu obiektu do bazy danych.
        self.save()
