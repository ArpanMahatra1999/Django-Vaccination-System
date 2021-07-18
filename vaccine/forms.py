from django import forms

from vaccine.models import Schedule


class UpdateScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['vaccinated']