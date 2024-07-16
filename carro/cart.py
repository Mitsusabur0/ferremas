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