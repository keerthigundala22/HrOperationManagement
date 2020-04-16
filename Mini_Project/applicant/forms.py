from  django import forms
from applicant.models import AppicantLogin,ApplicantRegistration

class ApplicantForm(forms.ModelForm):
    class Meta:
        model=AppicantLogin
        fields="__all__"

class ApplicantRegistrationForm(forms.ModelForm):
    gen = (('male', 'Male'), ('female', 'FeMale'))
    Gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)
    class Meta:
        model=ApplicantRegistration
        fields="__all__"


class ApplicantApplicationForm(forms.ModelForm):
    gen=(('male','Male'),('female','FeMale'))
    Gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    class Meta:
        model=ApplicantRegistration
        fields="__all__"

