from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Scieżka do panelu administracyjnego Django.
    path('admin/', admin.site.urls),
    # Scieżka do aplikacji 'ai_app', która zawiera własną konfigurację URL (ai_app.urls).
    path('ai_app/', include('ai_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Dodanie obsługi plików statycznych zgodnie z konfiguracją w settings.py

# `static()` jest używana do obsługi plików statycznych i multimedialnych w trakcie developmentu.
# Dodaje ona obsługę URL-i dla plików statycznych, takich jak obrazy, JavaScript, CSS, itp.
# `MEDIA_URL` i `MEDIA_ROOT` są skonfigurowane w pliku settings.py projektu,
# określają ścieżkę URL oraz katalog na serwerze, gdzie przechowywane są pliki.
