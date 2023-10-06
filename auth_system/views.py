from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib import messages


@login_required
def homepage(request):
        user = request.user
        first_name = request.user.first_name
        last_name = request.user.last_name

        context = {
            'user': user,
            'first_name': first_name,
            'last_name': last_name,
        }
        return render(request, "homepage.html", context)

    

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid login credentials!")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {'form': form})



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('login')