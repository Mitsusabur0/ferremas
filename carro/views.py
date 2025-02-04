from django.shortcuts import render, get_object_or_404
from .cart import Cart
from tienda.models import Producto
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    cart = Cart(request)
    cart_productos = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    return render(request, "cart_summary.html", {"cart_productos":cart_productos, "quantities":quantities, "totals":totals})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        producto_id = int(request.POST.get("producto_id"))
        producto_qty = int(request.POST.get("producto_qty"))
        producto = get_object_or_404(Producto, id=producto_id)
        cart.add(producto=producto, quantity=producto_qty)
    
        cart_quantity = cart.__len__()

        # response = JsonResponse({"Nombre del producto: ": producto.name})
        response = JsonResponse({"qty": cart_quantity})
        messages.success(request, ("Producto agregado al carro"))
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        producto_id = int(request.POST.get("producto_id"))
        cart.delete(producto=producto_id)

        response = JsonResponse({"producto":producto_id})
        messages.success(request, ("Producto eliminado del carro"))
        return response



def cart_update(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        producto_id = int(request.POST.get("producto_id"))
        producto_qty = int(request.POST.get("producto_qty"))

    cart.update(producto=producto_id, quantity=producto_qty)

    response = JsonResponse({"qty":producto_qty})
    messages.success(request, ("Se ha actualizado la cantidad"))
    return response
    # return redirect("cart_summary")
