from tienda.models import Producto

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_key")
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}
        self.cart = cart


    def add(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            pass
        else:
            self.cart[producto_id] = {"Precio": str(producto.price)}
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    
    def get_prods(self):
        producto_ids = self.cart.keys()
        productos = Producto.objects.filter(id__in=producto_ids)

        return productos
