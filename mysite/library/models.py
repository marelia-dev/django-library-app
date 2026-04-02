from django.contrib.auth.models import User
from django.db import models
import uuid
from django.utils import timezone
from tinymce.models import HTMLField
from PIL import Image as PilImage
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_pics", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = PilImage.open(self.photo.path)
            min_side = min(img.width, img.height)
            left = (img.width - min_side) // 2
            top = (img.height - min_side) // 2
            right = left + min_side
            bottom = top + min_side
            img = img.crop((left, top, right, bottom))
            img = img.resize((300, 300), PilImage.LANCZOS)
            img.save(self.photo.path)


class Author(models.Model):
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    description = HTMLField(verbose_name=_("Description"), max_length=3000, default="")

    def display_books(self):
        return ", ".join(book.title for book in self.books.all())

    display_books.short_description = _("Author's books")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Genre(models.Model):
    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    summary = models.TextField(_("Summary"))
    isbn = models.CharField(_("ISBN"), max_length=13, unique=True)   # лучше CharField для ISBN
    author = models.ForeignKey(
        to="Author",
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )
    genre = models.ManyToManyField(
        to="Genre",
        verbose_name=_("Genre")
    )
    cover = models.ImageField(
        upload_to="covers",
        verbose_name=_("Cover"),
        null=True,
        blank=True
    )

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all())

    display_genre.short_description = _("Genres")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class BookInstance(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    book = models.ForeignKey(
        to="Book",
        on_delete=models.CASCADE,
        related_name="instances",
        verbose_name=_("Book")
    )

    LOAN_STATUS = (
        ('d', _('Administered')),
        ('t', _('Taken')),
        ('a', _('Available')),
        ('r', _('Reserved')),
    )

    status = models.CharField(
        choices=LOAN_STATUS,
        verbose_name=_("Status"),
        max_length=1,
        default='d'
    )
    due_back = models.DateField(
        verbose_name=_("Due back"),
        null=True,
        blank=True
    )
    reader = models.ForeignKey(
        to=User,
        verbose_name=_("Reader"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def is_overdue(self):
        return self.due_back and self.due_back < timezone.now().date()

    def __str__(self):
        return f"{self.book.title} - {self.uuid}"

    class Meta:
        verbose_name = _("Book instance")
        verbose_name_plural = _("Book instances")
        ordering = ['due_back']


class BookReview(models.Model):
    book = models.ForeignKey(
        to="Book",
        on_delete=models.SET_NULL,
        related_name="reviews",
        null=True,
        blank=True,
        verbose_name=_("Book")
    )
    reviewer = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Reviewer")
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date created"))
    content = models.TextField(verbose_name=_("Review content"))

    class Meta:
        verbose_name = _("Book review")
        verbose_name_plural = _("Book reviews")
        ordering = ['-date_created']