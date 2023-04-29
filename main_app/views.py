from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Patient, Medication, Dose
from .forms import MedForm, DoseInlineFormset

from datetime import date

# Create your views here.

# general views
def home (request) :
    return render(request, 'home.html')

def signup (request) :
    # handling POST request
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            return redirect('home')
        
    # handling GET request
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })


# patient views
@login_required
def patient_list (request) :
    patients = Patient.objects.filter(user=request.user).order_by('name')
    return render(request, 'patients/patient_list.html', {
        'patients': patients,
    })

@login_required
def patient_detail (request, patient_id) :
    patient = Patient.objects.filter(user=request.user).get(id=patient_id)
    return render(request, 'patients/patient_detail.html', {
        'patient': patient,
        'date': date,
    })

@login_required
def patient_history (request, patient_id) :
    patient = Patient.objects.filter(user=request.user).get(id=patient_id)
    return render(request, 'patients/patient_history.html', {
        'patient': patient,
    })

class PatientCreate (LoginRequiredMixin, CreateView) :
    model = Patient
    fields = ('name', 'species', 'dob')
    template_name = 'patients/patient_form.html'

    def form_valid (self, form) :
        form.instance.user = self.request.user
        return super().form_valid(form)

class PatientUpdate (LoginRequiredMixin, UpdateView) :
    fields = ('name', 'species', 'dob')
    template_name = 'patients/patient_form.html'

    def get_queryset (self) :
        return Patient.objects.filter(user=self.request.user)
    
class PatientDelete (LoginRequiredMixin, DeleteView) :
    success_url = '/patients/'
    template_name = 'patients/patient_confirm_delete.html'

    def get_queryset (self) :
        return Patient.objects.filter(user=self.request.user)
    

# medication views
@login_required
def medication_detail (request, medication_id) :
    medication = Medication.objects.filter(user=request.user).get(id=medication_id)
    dose_form = DoseInlineFormset()
    return render(request, 'medications/medication_detail.html', {
        'medication': medication,
        'dose_form': dose_form,
        'date': date,
    })

@login_required
def medication_create (request) :
    # handling POST request
    if request.method == 'POST' :
        dose_form = DoseInlineFormset(request.POST)
        med_form = MedForm(request.POST)
        if med_form.is_valid() and dose_form.is_valid () :
            # if med_form.instance.day_supply == None :
            #     times_per_day = 24 / dose_form.time_interval
            #     amount_per_day = dose_form.amount * times_per_day
            #     day_supply = med_form.instance.quantity / amount_per_day
            #     med_form.instance.day_supply = day_supply
            med_form.instance.user = request.user
            instance = med_form.save()
            dose_form.instance = instance
            dose_form.save()
            return redirect('patient_detail', patient_id=instance.patient.id)

    # handling GET request
    med_form = MedForm()
    dose_form = DoseInlineFormset()
    return render(request, 'medications/medication_form.html', {
        'med_form': med_form,
        'dose_form': dose_form,
    })

@login_required
def medication_inactivate (request, medication_id) :
    medication = Medication.objects.get(id=medication_id)
    medication.is_active = False
    medication.inactive_date = date.today().isoformat()
    medication.save()
    return redirect('patient_detail', patient_id=medication.patient.id)

@login_required
def medication_activate (request, medication_id) :
    medication = Medication.objects.get(id=medication_id)
    medication.is_active = True
    medication.inactive_date = None
    medication.save()
    return redirect('patient_detail', patient_id=medication.patient.id)

class MedicationUpdate (LoginRequiredMixin, UpdateView) :
    fields = ('name', 'quantity', 'unit', 'day_supply', 'start_date', 'refills', 'patient')
    template_name = 'medications/medication_form.html'

    def get_queryset (self) :
        return Medication.objects.filter(user=self.request.user)
    
class MedicationDelete (LoginRequiredMixin, DeleteView) :
    template_name = 'medications/medication_confirm_delete.html'

    def get_queryset (self) :
        return Medication.objects.filter(user=self.request.user)
    
    def get_success_url (self) :
        patient = self.object.patient 
        return reverse_lazy('patient_detail', kwargs={'patient_id':patient.id})
    

# dose views
@login_required
def dose_create (request, medication_id) :
    dose_form = DoseInlineFormset(request.POST)

    if dose_form.is_valid () :
        dose_form.instance = Medication.objects.get(id=medication_id)
        dose_form.save()

    return redirect('medication_detail', medication_id=medication_id)

@login_required
def dose_delete (request, medication_id, dose_id) :
    dose = Dose.objects.get(id=dose_id)
    medication = Medication.objects.get(id=medication_id)
    
    if request.method == 'POST' :
        dose.delete()
        return redirect('medication_detail', medication_id=medication.id)
    
    return render(request, 'doses/dose_confirm_delete.html', {
        'dose': dose,
        'medication': medication
    })
