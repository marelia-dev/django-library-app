import uuid
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    description = models.TextField(default="")

    def display_books(self):
        return ', '.join(book.title for book in self.books.all())

    display_books.short_description = 'Books'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(verbose_name="Pavadinimas")

    class Meta:
        verbose_name = "Zanras"
        verbose_name_plural = "Zanrai"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField()
    summary = models.TextField()
    isbn = models.IntegerField()
    author = models.ForeignKey(
        to="Author", verbose_name="Author",
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name="books"
    )
    genre = models.ManyToManyField(to="Genre")

 
    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all())

    display_genre.short_description = "Zanrai"

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    book = models.ForeignKey(to="Book", on_delete=models.CASCADE)

    LOAN_STATUS = (
        ('d', 'Administered'),
        ('t', 'Taken'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(choices=LOAN_STATUS, default='d')
    due_back = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.uuid)

