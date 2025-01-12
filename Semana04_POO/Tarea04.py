class Producto: #clase de un producto en la tienda
    def __init__(self, nombre, precio, stock): #atributos del producto

        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):

        #informacion del producto
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Stock disponible: {self.stock} unidades")

    def actualizar_stock(self, cantidad_vendida):
        #stock total del producto despues de una venta
        if cantidad_vendida <= self.stock:
            self.stock -= cantidad_vendida
            print(f"Se vendieron {cantidad_vendida} unidades de {self.nombre}. Stock actualizado.")
        else:
            print(f"Error: No hay suficiente stock de {self.nombre}.")


class Carrito: #clase carrito de venta

    def __init__(self):
        #carrito de compras vacio
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        #agrego producto con cantidad especificada
        if cantidad > 0:
            self.productos.append({'producto': producto, 'cantidad': cantidad})
            print(f"Producto {producto.nombre} agregado al carrito. Cantidad: {cantidad}.")
        else:
            print("La cantidad debe ser mayor que 0.")

    def calcular_total(self):
        #calcular total compra
        total = 0
        for item in self.productos:
            total += item['producto'].precio * item['cantidad']
        return total

    def mostrar_carrito(self):
        #visualizacion de prodcutos totales en el carrito de compras
        if self.productos:
            print("\nProductos en el carrito:")
            for item in self.productos:
                print(f"- {item['producto'].nombre}: {item['cantidad']} unidades")
        else:
            print("El carrito está vacío.")#si el carro est vacio

    def realizar_compra(self):
        #compra mas actualizacion del stock
        total = self.calcular_total()
        print(f"\nTotal a pagar: ${total:.2f}")

        for item in self.productos:
            item['producto'].actualizar_stock(item['cantidad'])

        self.productos.clear()  # Vaciar el carrito después de la compra
        print("Compra realizada con éxito.")


# productos creados
producto1 = Producto("Laptop", 1000, 10)
producto2 = Producto("Smartphone", 500, 20)
producto3 = Producto("Auriculares", 150, 50)

# informacion productos
producto1.mostrar_info()
producto2.mostrar_info()
producto3.mostrar_info()

# carrito de compras mas productos
carrito = Carrito()
carrito.agregar_producto(producto1, 2)
carrito.agregar_producto(producto2, 1)
carrito.agregar_producto(producto3, 3)

# Mostrar los productos en el carrito
carrito.mostrar_carrito()

# Realizar la compra
carrito.realizar_compra()