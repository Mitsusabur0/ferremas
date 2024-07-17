from django.urls import path
from . import views

urlpatterns = [
    path("payment_success", views.payment_success, name="payment_success"),
    path("checkout", views.checkout, name="checkout"),
    path("checkout_usd", views.checkout_usd, name="checkout_usd"),

]
