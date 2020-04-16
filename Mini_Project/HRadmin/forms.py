from django import forms
from HRadmin.models import HRAdmin,AddEmployee

class HRadminForm(forms.ModelForm):
    class Meta:
        model=HRAdmin
        fields="__all__"
class AddForm(forms.ModelForm):
    class Meta:
        model=AddEmployee
        fields="__all__"

