from django.db import models
from django.urls import reverse
from bookdetails.models import BookInfo


# Create your models here.

class genre (models.Model):
    book = models.ForeignKey(
        BookInfo, on_delete=models.CASCADE, related_name="browsingGenre", null=True)

    def __str__(self):
        return '{} -- {} '.format(self.book.bookName, self.book.genre)

class copiesSold (models.Model):
    book = models.ForeignKey(
        BookInfo, on_delete=models.CASCADE, related_name="browsingCopiesSold", null=True)

    def __str__(self):
        return '{} -- {} '.format(self.book.copiesSold, self.book.bookName)
