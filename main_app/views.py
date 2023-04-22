from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Patient

# Create your views here.

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

@login_required
def patient_list (request) :
    patients = Patient.objects.filter(user=request.user).order_by('name')
    return render(request, 'patients/patient_list.html', {
        'patients': patients
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