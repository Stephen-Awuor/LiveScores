# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fixture
from teams.models import Teams
from .forms import FixtureForm
from teams.forms import TeamsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def currrent_fixtures(request):
    fixtures = Fixture.objects.all().order_by('-match_date')
    return render(request, 'base/admin_dashboard.html', {'fixtures': fixtures})
@login_required
def add_fixture(request):
    if request.method == 'POST':
        form = FixtureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fixture successfully saved')
            return redirect('admin_dashboard')
    else:
        form = FixtureForm()
    return render(request, 'admin/add_fixture.html', {'form': form})

@login_required
def fixture_edit(request, fixture_id):
    fixture_obj = get_object_or_404(Fixture, pk=fixture_id)
    form = FixtureForm(request.POST or None, instance=fixture_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Changes successfully saved')
        return redirect('admin_dashboard') 
    return render(request, 'admin/edit_fixture.html', {'form': form, 'fixture_obj': fixture_obj})

@login_required
def fixture_delete(request, fixture_id):
    fixture_obj = get_object_or_404(Fixture, pk=fixture_id)
    if request.method == "POST":
        fixture_obj.delete()
        return redirect('admin_dashboard') 
    return render(request, 'admin/confirm_delete_fixture.html', {'fixture_obj': fixture_obj})
