from django.contrib import admin
from django.urls import path
from app1 import views

admin.site.site_header = "daksh website Admin"
admin.site.site_title = "Battleground mobile india Admin Portal"
admin.site.index_title = "Welcome to sandy and daksh game Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='app1'),
    path("about", views.about, name='app1'),
    path("contact", views.contact, name='app1'),
    path("services", views.services, name='app1'),
    path("servicespubg", views.servicespubg, name='app1'),
    path("add_data", views.add_data, name='app1'),

]
