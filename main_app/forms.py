from django.forms import ModelForm, inlineformset_factory
from .models import Medication, Dose

class MedForm (ModelForm) :
    class Meta :
        model = Medication
        fields = ('name', 'day_supply', 'is_active', 'patient')

DoseInlineFormset = inlineformset_factory(Medication, Dose, fields='__all__', extra=1, can_delete_extra=False)