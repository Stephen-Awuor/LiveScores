from django import forms
from .models import Fixture

class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ['home_team', 'away_team', 'match_date', 'home_score', 'away_score', 'status']
        widgets = {
            'match_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
