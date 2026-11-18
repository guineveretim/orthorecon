from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about-dr-mageza/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('patient-information/', views.patient_info, name='patient_info'),
    path('for-referring-doctors/', views.referrals, name='referrals'),
    path('research/', views.research, name='research'),
    path('faq/', views.faq, name='faq'),
    path('contact-appointments/', views.contact, name='contact'),
]