from django.shortcuts import render
from carro.cart import Cart
from pago.forms import ShippingForm
from pago.models import ShippingAddress
import json
import requests

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
        return render(request, "payment/checkout.html", {"cart_productos":cart_productos, "quantities":quantities, "totals":totals, "shipping_form":shipping_form, "currency": "CLP"})
    else:
        return render(request, "payment/checkout.html", {"cart_productos":cart_productos, "quantities":quantities, "totals":totals, "shipping_form":False, "currency":"CLP"})




def checkout_usd(request):
    res = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
    rates = json.loads(res.text)
    usd = rates["rates"]["CLP"]

    cart = Cart(request)


    cart_productos = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    totals = round(float(totals)/usd, 2)
    

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html", {"cart_productos":cart_productos, "quantities":quantities, "totals":totals, "shipping_form":shipping_form, "usd":usd, "currency":"USD"})
    else:
        return render(request, "payment/checkout.html", {"cart_productos":cart_productos, "quantities":quantities, "totals":totals, "shipping_form":False, "usd":usd,"currency":"USD"})



