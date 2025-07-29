from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tentang/', views.about, name='about'),
    path('layanan/', views.services, name='services'),
    path('portofolio/', views.portfolio, name='portfolio'),
    path('tim/', views.team, name='team'),
    path('kontak/', views.contact, name='contact'),
]
