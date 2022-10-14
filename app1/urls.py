from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='app1'),
    path("about", views.about, name='app1'),
    path("contact", views.contact, name='app1'),
    path("services", views.services, name='app1'),
]
