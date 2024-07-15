from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    return render(request, "home.html", {"productos":productos});

def about(request):
    return render(request, "about.html");

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Sesión iniciada exitosamente."))
            return redirect("home")
        else:
            messages.success(request, ("Error al iniciar sesión, intente nuevamente."))
            return redirect("login")
    else:
        return render(request, "login.html", {})




    return render(request, "login.html");

def logout_user(request):
    logout(request)
    messages.success(request, ("Sesión cerrada exitosamente."))
    return redirect("home")


