from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TeamsForm
from .models import Teams


# Create your views here
@login_required
def current_teams(request):
    teams = Teams.objects.all()
    return render(request, 'admin/current_teams.html', {'teams': teams})

@login_required
def add_team(request):
    if request.method == 'POST':
        form = TeamsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Team item added successfully!")
            form = TeamsForm()  # reset the form
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TeamsForm()
    return render(request, 'admin/add_team.html', {'form': form})

@login_required
def team_edit(request, team_id):
    team_obj = get_object_or_404(Teams, pk=team_id)
    form = TeamsForm(request.POST or None, instance=team_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Changes successfully saved')
        return redirect('current-teams') 
    return render(request, 'admin/edit_team.html', {'form': form, 'team_obj': team_obj})

@login_required
def team_delete(request, team_id):
    team_obj = get_object_or_404(Teams, pk=team_id)
    if request.method == "POST":
        team_obj.delete()
        return redirect('current-teams') 
    return render(request, 'admin/confirm_delete_team.html', {'team_obj': team_obj})

