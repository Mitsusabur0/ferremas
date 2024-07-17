from django.shortcuts import render, redirect
from .models import Producto, Categoria, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from pago.forms import ShippingForm
from pago.models import ShippingAddress
from django import forms
from django.http import JsonResponse
from .serializers import ProductoSerializer
import json
import requests



# Create your views here.
def home(request):
    productos = Producto.objects.all()
    res = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
    rates = json.loads(res.text)
    usd = rates["rates"]["CLP"]
    return render(request, "home.html", {"productos":productos, "usd":usd})

def producto_list(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return JsonResponse({"Productos": serializer.data}, safe=False)

def producto_json(request, pk):
    producto = Producto.objects.get(id=pk)
    serializer = ProductoSerializer(producto)
    return JsonResponse({"Producto": serializer.data}, safe=False)

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, "Se ha actualizado la información")
            return redirect("home")
        return render(request, "update_info.html", {"form":form, "shipping_form":shipping_form})
    else:
        messages.success(request, "Debe iniciar sesión primero.")
        return redirect("home")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Contraseña actualizada correctamente.")
                login(request, current_user)
                return redirect("update_user")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect("update_password")
        else: 
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {"form":form});
    else:
        messages.success(request, ("Debes iniciar sesión."))
        return redirect("home")



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
            messages.success(request, ("Usuario creado. Agregue su información personal."))
            return redirect("update_info")
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



def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "Se ha actualizado el perfil de usuario.")
            return redirect("home")
        return render(request, "update_user.html", {"user_form":user_form})
    else:
        messages.success(request, "Debe iniciar sesión primero.")
        return redirect("home")
