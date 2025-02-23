from Inventario import Inventario
from Producto import Producto

def menu ():
    inventario=Inventario()
    while True:
        print("\n** Menu **")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            id_producto=int (input("Ingrese el ID del producto: "))
            nombre=str(input("Ingrese el nombre del producto: "))
            cantidad=int(input("Ingrese la cantidad del producto: "))
            precio=float(input("Ingrese el precio del producto: "))
            producto=Producto(id_producto, nombre, cantidad,precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = int(input("Ingrese el ID del producto a eliminar"))
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del produtco a actualizar "))
            nueva_cantidad=input("Nueva cantidad(Vacio si no quiere cambiar )")
            nuevo_precio=input("Nuevo precio(Vacio si no quiere cambiar )")
            nueva_cantidad=int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio=float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto,nueva_cantidad,nuevo_precio)
        elif opcion == "4":
            nombre =input("Ingresar el nombre del producto a buscar")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Bye Bye")
            break

        else:
            print("Opcion incorrecta")

if __name__ == "__main__":
    menu()


