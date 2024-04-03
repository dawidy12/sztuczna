from django.contrib import admin
from .models import ImageElement
from .models import TextElement
from .models import Book

admin.site.register(ImageElement)
admin.site.register(TextElement)
admin.site.register(Book)
