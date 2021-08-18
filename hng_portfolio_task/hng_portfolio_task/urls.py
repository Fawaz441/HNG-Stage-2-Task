from django.contrib import admin
from django.urls import path
from .views import homepage

urlpatterns = [
    path('res-asume1234/', admin.site.urls),
    path('',homepage,name='homepage')
]
