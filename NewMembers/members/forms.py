from django import forms
from .models import Miembro

class MemberForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = '__all__'
