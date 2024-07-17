from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True, )
    address1 = models.CharField(max_length=200, blank=True)
    # address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)



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
    price = models.DecimalField(default=0, decimal_places=0, max_digits=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    marca = models.CharField(max_length=100, default="Genérico")
    image = models.ImageField(upload_to="uploads/producto")
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=10)

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



