from django.contrib import admin

# Register your models here.
from .models import Book,Person

admin.site.register(Book)
admin.site.register(Person)
