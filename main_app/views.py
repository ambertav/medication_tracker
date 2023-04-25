from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Patient, Medication, Dose
from .forms import MedForm, DoseInlineFormset

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
        'form': form
    })


# patient views
@login_required
def patient_list (request) :
    patients = Patient.objects.filter(user=request.user).order_by('name')
    return render(request, 'patients/patient_list.html', {
        'patients': patients
    })

@login_required
def patient_detail (request, patient_id) :
    patient = Patient.objects.filter(user=request.user).get(id=patient_id)
    return render(request, 'patients/patient_detail.html', {
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
    return render(request, 'medications/medication_detail.html', {
        'medication': medication
    })

@login_required
def medication_create (request) :
    # handling POST request
    if request.method == 'POST' :
        dose_form = DoseInlineFormset(request.POST)
        med_form = MedForm(request.POST)
        if med_form.is_valid() and dose_form.is_valid () :
            med_form.instance.user = request.user
            instance = med_form.save()
            dose_form.instance = instance
            dose_form.save()
            return redirect('patient_list')

    # handling GET request
    med_form = MedForm()
    dose_form = DoseInlineFormset()
    return render(request, 'medications/medication_form.html', {
        'med_form': med_form,
        'dose_form': dose_form,
    })