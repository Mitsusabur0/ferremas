from django.shortcuts import render, get_object_or_404
from .cart import Cart
from tienda.models import Producto
from django.http import JsonResponse


def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        producto_id = int(request.POST.get("producto_id"))
        producto = get_object_or_404(Producto, id=producto_id)
        cart.add(producto=producto)

        cart_quantity = cart.__len__()

        # response = JsonResponse({"Nombre del producto: ": producto.name})
        response = JsonResponse({"qty": cart_quantity})
        return response
    
        





def cart_delete(request):
    pass

def cart_update(request):
    pass


