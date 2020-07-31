from django.contrib import admin
from .models import BookInfo
from .models import BookAuthor
# Register your models here.

admin.site.register(BookInfo)
admin.site.register(BookAuthor)
