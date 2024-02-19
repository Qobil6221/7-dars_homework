from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.shared.forms import LoginForm, UserRegistrationForm


def home_page(request):
    return render(request, 'books/home.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                messages.success(request, f'{request.user.username} User succesfully loged in')
                return redirect('home')
            else:
                messages.warning(request, 'User not found')
                return redirect('users:login')
        else:
            return render(request, 'books/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'books/login.html', {'form': form})


def register_view(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully registered')
            return redirect('users:login')
        else:
            return render(request, 'books/register.html', {'form': form})
    else:
        return render(request, 'books/login.html', {'form': form})


def profile_view(request):
    return render(request, 'books/profile.html')


@login_required
def logout_view(request):
    messages.info(request, f'{request.user.username}  User successfulley loged out!')
    logout(request)
    return redirect('home')
