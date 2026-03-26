from django.contrib.auth.models import User
from django.db import models
import uuid


class Author(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    description = models.TextField(default="")

    def display_books(self):
        return ", ".join(book.title for book in self.books.all())

    display_books.short_description = "Autoriaus knygos"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(verbose_name="Pavadinimas")

    class Meta:
        verbose_name = "Žanras"
        verbose_name_plural = "Žanrai"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField()
    summary = models.TextField()
    isbn = models.IntegerField()
    author = models.ForeignKey(to="Author",
                               on_delete=models.SET_NULL,
                               null=True, blank=True,
                               related_name='books')
    genre = models.ManyToManyField(to="Genre")
    cover = models.ImageField(upload_to="covers", null=True, blank=True)

    # def display_genre(self):
    #     genres = self.genre.all()
    #     result = ""
    #     for genre in genres:
    #         result += genre.name + ", "
    #     return result

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all())

    display_genre.short_description = "Žanrai"

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    book = models.ForeignKey(to="Book", on_delete=models.CASCADE, related_name="instances")

    LOAN_STATUS = (
        ('d', 'Administered'),
        ('t', 'Taken'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(choices=LOAN_STATUS, default="d")
    due_back = models.DateField(null=True, blank=True)
    reader = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return str(self.uuid)