from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from teams.models import Teams
from fixtureadmin.models import Fixture

# Create your views here.

def dashboard(request):
    fixtures = Fixture.objects.all()
    return render(request, 'viewer/livescore.html' , {'teams': fixtures})

def season_teams(request):
    teams = Teams.objects.all()
    return render(request, 'viewer/teams.html' , {'teams': teams})

