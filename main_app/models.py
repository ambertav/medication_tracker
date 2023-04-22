from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    day_supply = models.IntegerField(default=30)
    is_active = models.BooleanField(default=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self) :
        return self.name
