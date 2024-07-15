from django.shortcuts import render
from .models import Producto


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    return render(request, "home.html", {"productos":productos});


def about(request):
    return render(request, "about.html");


