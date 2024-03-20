# Importuje klasę models z modułu django.db
from django.db import models
# Importuje default_storage z modułu django.core.files.storage
from django.core.files.storage import default_storage
# Importuje moduł image z tensorflow.keras.preprocessing i przypisuje mu alias tf_image
from tensorflow.keras.preprocessing import image as tf_image
# Importuje klasy i funkcje z inception_v3
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
# Importuje moduł numpy i przypisuje mu alias np
from django.core.files.base import ContentFile  # Importuje klasę ContentFile z django.core.files.base
import numpy as np


class ImageElement(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="mediaphoto", blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            try:  # Rozpoczyna blok try
                file_path = self.photo.path
                if default_storage.exists(file_path):
                    # Ładuje obraz o zadanych wymiarach
                    pil_image = tf_image.load_img(file_path, target_size=(299, 299))
                    # Konwertuje obraz na tablicę numpy
                    img_array = tf_image.img_to_array(pil_image)
                    # Rozszerza tablicę o nowy wymiar
                    img_array = np.expand_dims(img_array, axis=0)
                    # Przetwarza obraz zgodnie z wymaganiami modelu
                    img_array = preprocess_input(img_array)

                    # Tworzy model InceptionV3
                    model = InceptionV3(weights='imagenet')
                    # Dokonuje predykcji na obrazie
                    predictions = model.predict(img_array)
                    # Dekoduje predykcje
                    decoded_predictions = decode_predictions(predictions, top=1)[0]
                    # Wybiera najbardziej prawdopodobną etykietę
                    best_guess = decoded_predictions[0][1]
                    # Ustawia tytuł na najbardziej prawdopodobną etykietę
                    self.title = best_guess
                    # Tworzy łańcuch znaków zawierający etykiety i prawdopodobieństwa predykcji
                    self.content = ', '.join([f"{pred[1]}: {pred[2] * 100:.2f}%" for pred in decoded_predictions])
                    super().save(*args, **kwargs)

            except Exception as e:  # Obsługuje wyjątek
                # Nic nie robi w przypadku wystąpienia wyjątku
                pass
