from django.db import models
import datetime

# Modelo de Categorias de productos
class Categoria(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Modelo de Clientes
class Cliente(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Modelo de Productos
class Producto(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default="", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/producto")

    def __str__(self):
        return self.name


# Modelo de Pedidos
class Pedido(models.Model):
    producto =
    cliente =
    quantity = 
    address = 
    phone =
    date = 
    status = 

    def __str__(self):
        return self.product



