from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.

def dashboard(request):
    return render(request, 'viewer/livescore.html')

def previous_matches(request):
    return render(request, 'viewer/previous_fixtures.html')

def upcoming_matches(request):
    return render(request, 'viewer/upcoming_fixtures.html')

def season_teams(request):
    return render(request, 'viewer/teams.html')

