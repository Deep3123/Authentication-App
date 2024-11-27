from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .forms import SignUpForm

# Login view
def login_view(request):
    if request.user.is_authenticated:  # Redirect logged-in users to the dashboard
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Signup view
def signup_view(request):
    if request.user.is_authenticated:  # Redirect logged-in users to the dashboard
        return redirect('dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Forgot password view (stub)
def forgot_password_view(request):
    # You can implement password reset logic here in the future
    return render(request, 'accounts/forgot_password.html')

# Change password view
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in after changing password
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

# Dashboard view
@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

# Profile view
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')