from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from datetime import date

# Create your models here.

class Patient (models.Model) :
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    dob = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self) :
        return self.name
    
    def get_absolute_url (self) :
        return reverse('patient_detail', kwargs={'patient_id':self.id})
    
class Medication (models.Model) :
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=30)
    day_supply = models.PositiveIntegerField(blank=True, null=True)
    refills = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    start_date = models.DateField(default=date.today)
    is_active = models.BooleanField(default=True)
    inactive_date = models.DateField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self) :
        return self.name
    
    def get_absolute_url (self) :
        return reverse('medication_detail', kwargs={'medication_id':self.id})

class Dose (models.Model) :
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    time_of_adminstration = models.TimeField()
    time_interval = models.IntegerField()
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

    def __str__ (self) :
        return f'{self.amount} {self.unit}'