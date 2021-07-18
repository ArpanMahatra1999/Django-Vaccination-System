from django import forms

from child.models import Child


class CreateChildForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = ('parent',)
        widgets = {
            'place_of_birth': forms.Textarea(attrs={'rows': 1}),
            'place_of_vaccination': forms.Textarea(attrs={'rows': 1})
        }


class UpdateChildForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = ('parent',)
        widgets = {
            'place_of_birth': forms.Textarea(attrs={'rows': 1}),
            'place_of_vaccination': forms.Textarea(attrs={'rows': 1})
        }