from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('result',views.result,name='result'),
    path('add',views.add, name='result'),
    path('custmer',views.custmer,name='custmer'),
    path('Add1',views.Add1, name='custmer'),
    path('final',views.final, name='final'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services')
    
    
    

]