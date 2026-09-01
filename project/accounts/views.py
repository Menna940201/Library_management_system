from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def signup_view(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Account created successfully!")
    #         return redirect('book_list')
    #     else:
    #         messages.error(request, "Please correct the errors below.")
    # else:
    #     form = SignUpForm()
    # return render(request, 'accounts/signup.html', {'form': form})
    if request.method == 'POST':
        username = request.POST.get('username','').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/signup.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'accounts/signup.html')
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('book_list')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')