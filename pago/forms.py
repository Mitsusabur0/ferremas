from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):

    shipping_full_name = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}), required=True)
    shipping_address1 = forms.CharField(label="Dirección", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección:'}), required=True)
    shipping_address2 = forms.CharField(label="Detalles Direccción", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalles Dirección:'}), required=False)
    shipping_city = forms.CharField(label="Ciudad", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad'}), required=True)
    shipping_state = forms.CharField(label="Región", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Región'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ["shipping_full_name", "shipping_address1", "shipping_address2", "shipping_city", "shipping_state"]
        exclude= ["user",]

