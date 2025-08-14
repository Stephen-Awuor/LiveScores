from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TeamsForm

# Create your views here
@login_required
def current_teams(request):
    return render(request, 'admin/current_teams.html')

@login_required
def add_team(request):
    if request.method == 'POST':
        form = TeamsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Team item added successfully!")
            return redirect('current-teams')  
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TeamsForm()
    return render(request, 'admin/add_team.html', {'form': form})
