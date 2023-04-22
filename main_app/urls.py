from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/create/', views.PatientCreate.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_delete'),


    path('accounts/signup/', views.signup, name='signup'),
]