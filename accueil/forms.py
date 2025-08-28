from django import forms
from .models import Visiteur

class VisiteurForm(forms.ModelForm):
    class Meta:
        model = Visiteur
        fields = ['nom']
