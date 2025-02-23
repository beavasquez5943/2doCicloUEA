import os
import json
from Producto import Producto
class Inventario:
    ARCHIVO = "inventario.txt" #archivo de texto donde se guardara modificaciones


    def __init__(self):
        #lista vacia de productos
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as file:
                json.dump([p.to_dict() for p in self.productos], file)
            print("Inventario guardado correctamente")
        except PermissionError:
            print("No puede modificar el archivo")
        except  Exception as e:
            print(f"ERROR {e}")


    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            print("Archivo de inventario no encontrado.")
            return
        try:
                with open(self.ARCHIVO, "r") as file:
                    data = json.load(file)
                    self.productos = [Producto.from_dict(d) for d in data]
                print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Error: El archivo de inventario no existe.")

        except json.JSONDecodeError:
            print("Error: El archivo de inventario está corrupto o vacío.")

        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")


    #agrega un producto por su ID
    def añadir_producto (self, producto: Producto):

        for p in self.productos:
            #agrega nuevo producto al inventario
            if p.get_id()==producto.get_id():
                print("El ID del producto ya existe")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado correctemente")

    #elimina un producto por su ID
    def eliminar_producto(self,id_prodcuto:int):
        inicial_len= len(self.productos)

        self.productos= [p for p in self.productos
                         if p.get_id() != id_prodcuto]
        print(f"Producto con ID {id_prodcuto} ELIMINADO")

        if len(self.productos) < inicial_len:
            self.guardar_en_archivo()
            print(f"Producto con ID {id_prodcuto} eliminado.")
        else:
            print(f"No se encontró un producto con ID {id_prodcuto}.")


    #Actualiza la informacion de un producto
    def actualizar_producto(self, id_producto: int, nueva_cantidad: int = None, nuevo_precio: float = None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre: str):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)

# Métodos en la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {"id": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
