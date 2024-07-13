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
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=15, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product



