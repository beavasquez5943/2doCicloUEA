class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # gestion libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()
        self.historial_prestamos = {}

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.historial_prestamos[usuario.id_usuario] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            if not self.historial_prestamos[id_usuario]:
                self.usuarios.remove(id_usuario)
                del self.historial_prestamos[id_usuario]
                print(f"Usuario con ID {id_usuario} dado de baja.")
            else:
                print("El usuario tiene libros prestados. No puede darse de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            self.historial_prestamos[id_usuario].append(self.libros.pop(isbn))
            print(f"Libro con ISBN {isbn} prestado al usuario {id_usuario}.")
        else:
            print("El usuario no está registrado o el libro no está disponible.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and any(libro.isbn == isbn for libro in self.historial_prestamos[id_usuario]):
            libro_devuelto = next(libro for libro in self.historial_prestamos[id_usuario] if libro.isbn == isbn)
            self.historial_prestamos[id_usuario].remove(libro_devuelto)
            self.libros[isbn] = libro_devuelto
            print(f"Libro con ISBN {isbn} devuelto por usuario {id_usuario}.")
        else:
            print("El usuario no tiene prestado ese libro.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio, None) == valor]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            print(f"Libros prestados a usuario {id_usuario}: {self.historial_prestamos[id_usuario]}")
        else:
            print("Usuario no encontrado.")


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nSistema de Gestión de Biblioteca Digital")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))
        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, id_usuario))
        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)
        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)
        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)
        elif opcion == "7":
            criterio = input("Buscar por (titulo, autor, categoria): ")
            valor = input("Ingrese el valor de búsqueda: ")
            biblioteca.buscar_libro(criterio, valor)
        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()

