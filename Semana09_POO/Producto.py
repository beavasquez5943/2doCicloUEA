class Producto:
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

        #Definicion del producto
        def __str__(self):
            return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

        #Getters y Setters
        def get_id (self):
            return self.id_producto

        def get_nombre (self):
            return self.nombre

        def get_cantidad (self):
            return self.cantidad
        def get_precio (self):
            return self.precio
        def set_cantidad (self,cantidad):
            self.cantidad=cantidad
        def set_precio (self,precio):
            self.precio=precio
