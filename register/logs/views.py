from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import request, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'logs/login.html', {"message": None})

    return render(request, 'logs/user.html', {'message': request.user})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'logs/login.html', {'message': 'not valid'})


def logout_view(request):
    logout(request)
    return render(request, "logs/login.html", {"message": "Logged out."})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        raw_password1 = request.POST['password1']
        raw_password2 = request.POST['password2']
        if len(raw_password1) <8 :
            form = UserCreationForm()
            return render(request, 'logs/register.html', {'form': form, 'message':'too short password'})

        if raw_password1 !=raw_password2:
            form = UserCreationForm()
            return render(request, 'logs/register.html', {'form': form, 'message': 'passwords not equal'})

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render(request, 'logs/register.html', {'form': form, 'message': ''})
