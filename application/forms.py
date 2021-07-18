from django import forms

from application.models import Application


class CreateApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['vaccine']