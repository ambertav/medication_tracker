from django.forms import ModelForm, inlineformset_factory
from .models import Medication, Dose

class MedForm (ModelForm) :
    class Meta :
        model = Medication
        exclude = ('is_active', 'inactive_date', 'user')

DoseInlineFormset = inlineformset_factory(Medication, Dose, exclude=('medication', 'is_active', 'inactive_date'), extra=1, can_delete_extra=False)