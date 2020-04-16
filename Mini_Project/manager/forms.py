from  django import forms
from manager.models import ManagerModel, RecuirtmentModel, Applicant


class ManagerForm(forms.ModelForm):
    class Meta:
        model=ManagerModel
        fields="__all__"

class RecuirtmentForm(forms.ModelForm):
    class Meta:
        model=RecuirtmentModel
        fields="__all__"
class ApplicantForm(forms.ModelForm):
    class Meta:
        model=Applicant
        fields="__all__"