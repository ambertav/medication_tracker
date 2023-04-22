from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create', views.PatientCreate.as_view(), name='patient_create'),


    path('accounts/signup/', views.signup, name='signup'),
]