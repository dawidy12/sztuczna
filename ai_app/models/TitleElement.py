# myapp/models.py

from django.db import models
import openai
import os
# Ustaw swój klucz API OpenAI tutaj
openai.api_key = os.environ.get('OPENAI_API_KEY')


def generate_description_from_title(title):
    try:
        # Wywołanie GPT-3 z użyciem klucza API, przekazując tytuł jako część monitu
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Zaktualizowana nazwa modelu
            prompt=f"Generate a descriptive text based on the following title: {title}\n",
            temperature=0.7,
            max_tokens=100
        )
        # Zwróć tekst wygenerowany przez GPT-3 jako opis
        return response.choices[0].text.strip()
    except Exception as e:
        # W przypadku błędu zwróć komunikat błędu lub domyślny opis
        print(f"Error generating description: {str(e)}")
        return "{}".format(e)


class TextElement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generuj opis tylko jeśli content jest pusty
        if not self.content:
            self.content = generate_description_from_title(self.title)
        super().save(*args, **kwargs)
