from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fixtureadmin.models import Fixture
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import AdminProfileForm
from django.contrib.auth.hashers import check_password

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
        form = AuthenticationForm()
    return render(request, "admin/login.html", {"form": form})

@login_required
def admin_dashboard(request):
    fixtures = Fixture.objects.all().order_by('-match_date')
    return render(request, 'base/admin_dashboard.html', {'fixtures': fixtures})

def admin_logout(request):
    logout(request)
    return redirect('/')  

@login_required
def manage_profile(request):
    if request.method == 'POST':
        form = AdminProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)

            # password handling
            old_password = form.cleaned_data.get("old_password")
            new_password = form.cleaned_data.get("new_password")

            if new_password:
                if not check_password(old_password, request.user.password):
                    messages.error(request, "Old password is incorrect.")
                    return redirect('manage-profile')
                user.set_password(new_password)

            user.save()
            update_session_auth_hash(request, user)  # keeps admin logged in
            messages.success(request, "Profile updated successfully.")
            return redirect('manage-profile')
    else:
        form = AdminProfileForm(instance=request.user)

    return render(request, 'admin/admin_profile.html', {'form': form})