from django.urls import path
from hello import views
from django.contrib import admin
urlpatterns = [
   path('admin/', admin.site.urls),
]