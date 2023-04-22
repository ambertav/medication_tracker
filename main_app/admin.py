from django.contrib import admin

from .models import Patient, Medication, Dose

# Register your models here.

admin.site.register([Patient, Medication, Dose])