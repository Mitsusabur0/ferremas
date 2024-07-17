from django.shortcuts import render
from carro.cart import Cart
from pago.forms import ShippingForm
from pago.models import ShippingAddress

def payment_success(request):

    return render(request, "payment/payment_success.html", {})


def checkout(request):
    cart = Cart(request)
    cart_productos = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html", {"cart_productos":cart_productos, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        return render(request, "payment/checkout.html", {"cart_productos":cart_productos, "quantities":quantities, "totals":totals, "shipping_form":False})





