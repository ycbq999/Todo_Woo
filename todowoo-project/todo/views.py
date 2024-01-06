from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo


# Create your views here.

def home(request):
    return render(request, "todo/home.html")


def signupuser(request):

    if request.method == "GET":
        return render(request, "todo/signupuser.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:

            try:
                # Create a new user 
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                # Save the user
                user.save()
                # Login the user
                login(request, user)
                # Redirect to current todos page
                return redirect("currenttodos")
            except IntegrityError:
                return render(request, "todo/signupuser.html", {"form": UserCreationForm(), "error": "Username already been taken. Please choose a new username"})

        else:
            return render(request, "todo/signupuser.html", {"form": UserCreationForm(), "error": "Passwords did not match"})
        



def loginuser(request):
    if request.method == "GET":
        return render(request, "todo/loginuser.html", {"form": AuthenticationForm()})
    else:
        # Authenticate the user
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        # If user is not None
        if user is not None:
            # Login the user
            login(request, user)
            # Redirect to current todos page
            return redirect("currenttodos")
        else:
            return render(request, "todo/loginuser.html", {"form": AuthenticationForm(), "error": "Username and password did not match"})


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")

def createtodo(request):
    if request.method == "GET":
        return render(request, "todo/createtodo.html", {"form": TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect("currenttodos")
        except ValueError:
            return render(request, "todo/createtodo.html", {"form": TodoForm(), "error": "Bad data passed in. Try again."})



def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "todo/currenttodos.html",{ "todos": todos})