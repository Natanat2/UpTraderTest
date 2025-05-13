from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('services/', views.services_view, name='services'),
    path('services/web/', views.web_services_view, name='web_services'),
    path('services/mobile/', views.mobile_services_view, name='mobile_services'),
]
