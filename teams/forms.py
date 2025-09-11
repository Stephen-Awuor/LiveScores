# forms.py
from django import forms
from .models import Teams

class TeamsForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['team_name', 'sport', 'coach', 'email']
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
            'sport': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
            'coach': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
        }
