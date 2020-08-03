from django.contrib import admin
from .models import BookInfo
from .models import BookAuthor
from adminsortable.utils import get_is_sortable
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    search_fields=('bookISBN',)
    list_display = ('bookName', 'genre', 'copiesSold',)
    list_filter = ['genre']
    list_per_page = 4
    
    def bookName (self, obj):
        return obj.description

    def queryset(self, request):
        qs = super(BookInfoAdmin, self).queryset(request)
        qs = qs.order_by('-copiesSold',)
        return qs
    


admin.site.register (BookInfo,BookInfoAdmin)
admin.site.register (BookAuthor)