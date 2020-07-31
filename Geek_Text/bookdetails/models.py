from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class BookAuthor(models.Model):
    authorfirstName = models.CharField(max_length=100,default='')
    authorlastName=models.CharField(max_length=100,default='')
    authorBio = models.CharField(max_length=1000,default='')
    publisher = models.CharField(max_length=1000,default='')
    def __str__(self):
        return self.authorfirstName


class BookInfo(models.Model):
    author=models.ForeignKey(BookAuthor,on_delete=models.CASCADE,related_name="bookAuthor",null=True)
    bookName = models.CharField(max_length=100, unique=True,default='')
    description = models.CharField(max_length=1000,default='')
    genre = models.CharField(max_length=30,default='')
    price = models.DecimalField(max_digits=5, decimal_places=2,default='')
    publisher = models.CharField(max_length=1000,default='')
    bookISBN= models.CharField(max_length=100, unique=True,default='')
    yearPublished= models.CharField(max_length=5,default='')
    copiesSold=models.CharField(max_length=100000000,default='')


    def __str__(self):
        return self.bookName

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookRatings(models.Model):
    bookRating = models.CharField(max_length=1000)  # temporary


class Meta:
        ordering = ['price', 'bookName']