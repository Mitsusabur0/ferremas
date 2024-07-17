from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Producto, Categoria, Profile
from decimal import Decimal

class EcommerceTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.categoria = Categoria.objects.create(name='Test Category')
        self.producto = Producto.objects.create(
            name='Test Product',
            price=Decimal('100.00'),
            categoria=self.categoria
        )

    def test_producto_creation(self):
        # Verificar que se puede crear una instancia de Producto
        self.assertEqual(self.producto.name, 'Test Product')
        self.assertEqual(self.producto.price, Decimal('100.00'))
        self.assertEqual(self.producto.categoria, self.categoria)

    def test_profile_creation(self):
        # Verificar que se crea un perfil de usuario automaticamente al registrar un nuevo User
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_home_view(self):
        # Verificar que la view home retorne un status 200, usando el template correcto
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_view(self):
        # Verificar que un usuario pueda hacer login exitoso
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass123'})
        self.assertRedirects(response, reverse('home'))

    def test_producto_api_view(self):
        # Verificar que la API producto_json retorne la información correcta del producto
        response = self.client.get(reverse('producto_json', args=[self.producto.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['Producto']['name'], 'Test Product')
        self.assertEqual(Decimal(data['Producto']['price']), Decimal('100.00'))