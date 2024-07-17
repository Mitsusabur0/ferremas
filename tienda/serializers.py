from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'name', 'price', 'categoria', 'marca', 'is_sale', 'sale_price']
