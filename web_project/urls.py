"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account import views as v
from carts import views as vws


from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('manageAccount/', v.manageAccount, name="manageAccount"),
    path('viewCreditCards/', v.viewCC, name="viewCreditCards"),
    path('createCreditCard/', v.createCC, name="createCreditCard"),
    path('', include("django.contrib.auth.urls")),
    path('home_carts/', vws.home_carts, name="home_carts" )
    
]

   


