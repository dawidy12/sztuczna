from django.db import models  # Importuje klasy i metody Django do pracy z modelami bazy danych
import openai  # Importuje bibliotekę klienta OpenAI do interakcji z API OpenAI
import os  # Importuje moduł os do pracy z zmiennymi środowiskowymi systemu operacyjnego

# Ustaw swój klucz API OpenAI tutaj
openai.api_key = os.environ.get('OPENAI_API_KEY')  # Pobiera wartość zmiennej środowiskowej 'OPENAI_API_KEY' i przypisuje ją jako klucz API do klienta OpenAI

def generate_description_from_title(title):  # Definiuje funkcję, która generuje opis na podstawie podanego tytułu
    try:
        # Wywołanie GPT-3 z użyciem klucza API, przekazując tytuł jako część monitu
        response = openai.Completion.create(  # Wywołuje metodę create na obiekcie Completion z pakietu openai, aby uzyskać odpowiedź od modelu GPT-3
            engine="gpt-3.5-turbo-instruct",  # Określa model GPT-3 do wykorzystania
            prompt=f"Generate a descriptive text based on the following title: {title}\n",  # Definiuje monit dla modelu GPT-3, prosząc o wygenerowanie opisu na podstawie tytułu
            temperature=0.7,  # Ustawia temperaturę dla procesu generowania, wpływając na kreatywność odpowiedzi
            max_tokens=100  # Określa maksymalną liczbę tokenów, które model może wygenerować jako odpowiedź
        )
        # Zwróć tekst wygenerowany przez GPT-3 jako opis
        return response.choices[0].text.strip()  # Zwraca tekst wygenerowany przez model, usuwając białe znaki z początku i końca
    except Exception as e:
        # W przypadku błędu zwróć komunikat błędu lub domyślny opis
        print(f"Error generating description: {str(e)}")  # Wypisuje komunikat o błędzie do konsoli
        return "{}".format(e)  # Zwraca komunikat błędu jako opis

class TextElement(models.Model):  # Definiuje klasę TextElement jako model Django
    title = models.CharField(max_length=255)  # Pole 'title' typu CharField, przechowujące tytuł elementu tekstu
    content = models.TextField(blank=True)  # Pole 'content' typu TextField, przechowujące treść elementu tekstu; może być puste

    def __str__(self):  # Metoda specjalna, definiująca reprezentację tekstową instancji modelu
        return self.title  # Zwraca tytuł elementu tekstu jako jego reprezentację tekstową

    def save(self, *args, **kwargs):  # Nadpisuje metodę save, aby dostosować proces zapisu instancji modelu
        # Generuj opis tylko jeśli content jest pusty
        if not self.content:  # Sprawdza, czy pole 'content' jest puste
            self.content = generate_description_from_title(self.title)  # Jeśli tak, wywołuje funkcję generate_description_from_title, aby wygenerować i przypisać treść
        super().save(*args, **kwargs)  # Wywołuje oryginalną metodę save klasy nadrzędnej, aby zapisać zmiany w instancji modelu
