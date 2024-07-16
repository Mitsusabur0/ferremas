from tienda.models import Producto

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_key")
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}
        self.cart = cart


    def add(self, producto, quantity):
        producto_id = str(producto.id)
        producto_qty = str(quantity)
        if producto_id in self.cart:
            pass
        else:
            # self.cart[producto_id] = {"Precio": str(producto.price)}
            self.cart[producto_id] = int(producto_qty)
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    
    def get_prods(self):
        producto_ids = self.cart.keys()
        productos = Producto.objects.filter(id__in=producto_ids)
        return productos
    

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, producto, quantity):
        producto_id = str(producto)
        producto_qty = int(quantity)

        ourcart = self.cart
        ourcart[producto_id] = producto_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, producto):
        producto_id = str(producto)
        if producto_id in self.cart:
            del self.cart[producto_id]

        self.session.modified = True
