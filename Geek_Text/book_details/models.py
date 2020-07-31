from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money

# Using direct User model due to issues with Seeder
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField('Title of the book',max_length=200)
    author = models.ForeignKey(
        'Author',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    description = models.TextField(
        'Description of book contents and misc info',
        max_length=500,
        blank=True)
    price = MoneyField(
        'Price',
        max_digits=15,
        decimal_places=2,
        default_currency='USD',
        default=Money(0, 'USD'))
    genre = models.ForeignKey(
        'Genre',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    publisher = models.ForeignKey(
        'Publisher',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    publish_date = models.DateField(
        'Date publisher initially released current book version')
    cover = models.ImageField(
        'Front cover of book',
        upload_to = 'book_covers/',
        null=True)

    def __str__(self):
        return '{} -- {}'.format(self.author, self.title)

class Author(models.Model):
       first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    bio = models.CharField(null= True, max_length=10000)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('failed', null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        "Returns the url to get a particular author."
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        "String for representing the Model object."
        return '{0}, {1}'.format(self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(
        'Short name for genre',
        max_length=15)

    def __str__(self):
        return '{}'.format(self.name)

class Review(models.Model):
    book = models.ForeignKey(
        'Book',
        related_name='reviews')
    user = models.ForeignKey(
        User,
        related_name='reviews')
    anonymous = models.BooleanField(
        'Whether or not the comment was posted anonymously')
    rating = models.IntegerField(
        'Rating associated with user comment; implies a review of the Book',
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(
        'User submitted comment on the associated Book',
        max_length=500,
        blank=True)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return '{} -- {}'.format(self.book.title, self.user.username)