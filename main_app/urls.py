from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/create/', views.PatientCreate.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_delete'),

    path('medications/<int:medication_id>/', views.medication_detail, name='medication_detail'),
    path('medications/create/', views.medication_create, name='medication_create'),
    path('medications/<int:pk>/update/', views.MedicationUpdate.as_view(), name='medication_update'),
    path('medications/<int:pk>/delete/', views.MedicationDelete.as_view(), name='medication_delete'),

    path('medications/<int:medication_id>/inactivate/', views.medication_inactivate, name='medication_inactivate'),
    path('medications/<int:medication_id>/activate/', views.medication_activate, name='medication_activate'),

    path('medications/<int:medication_id>/dose/create/', views.dose_create, name='dose_create'),
    path('medications/<int:medication_id>/dose/<int:dose_id>/delete/', views.dose_delete, name='dose_delete'),

    path('accounts/signup/', views.signup, name='signup'),
]