from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fixtureadmin.models import Fixture

def admin_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')  # redirect after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "admin/login.html", {"form": form})

@login_required
def admin_dashboard(request):
    fixtures = Fixture.objects.all().order_by('-match_date')
    return render(request, 'base/admin_dashboard.html', {'fixtures': fixtures})

def admin_logout(request):
    logout(request)
    return redirect('/')  
