from django.contrib import admin
from books.models import Books
# Register your models here.

class BooksAdmin(admin.ModelAdmin):

    list_display = ["id", "title", "description"]

admin.site.register(Books, BooksAdmin)
