# Will store the different views of the website.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, TaskForm
from .decorators import unauthenticated_user, allowed_users

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'E-mail or Password is incorrect')

    context = {}
    return render(request, 'notification_calendar_app/login.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def home(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}

    return render(request, 'notification_calendar_app/calendar.html', context)
    # return render(request, 'notification_calendar_app/calendar.html')

@unauthenticated_user
def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')
            messages.success(request, "Congratulations {}, your account was created successfully!".format(name))
            return redirect('login')

    context = {'form': form}
    return render(request, 'notification_calendar_app/registration.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def UpdateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'notification_calendar_app/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'notification_calendar_app/delete.html', context)
