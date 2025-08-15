# forms.py
from django import forms
from .models import Teams

class TeamsForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'max-width:500px;'}))

    class Meta:
        model = Teams
        fields = ['team_name', 'age_group', 'gender', 'sport', 'coach', 'email']
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
            'age_group': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
            'sport': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
            'coach': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'max-width:500px;'}),
        }
