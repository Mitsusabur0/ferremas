from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


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

def logout_user(request):
    logout(request)
    messages.success(request, ("Sesión cerrada exitosamente."))
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Usuario creado exitosamente."))
            return redirect("home")
        else:
            messages.success(request, ("Error al registrar, intente nuevamente."))
            return redirect("register")
    else:
        return render(request, "register.html", {"form":form})

def producto(request, pk):
    producto = Producto.objects.get(id=pk)
    return render(request, "producto.html", {"producto":producto});


def categoria(request, foo):
    foo = foo.replace("-", " ")

    try:
        categoria = Categoria.objects.get(name=foo)
        if categoria == "":
            productos = Producto.objects.all()
            return render(request, "categoria.html", {"productos":productos, "categoria":"Todos los productos"})
        else:
            productos = Producto.objects.filter(categoria=categoria)
            return render(request, "categoria.html", {"productos":productos, "categoria":categoria})
    except:
        messages.success(request, ("Error en la selección de categorías"))
        return redirect("home")
    

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, "catalogo.html", {"productos":productos});