
class DocManager:

    def __init__(self, file_name, mode): #inicia el manejador de archivos


        #file_name: Nombre del archivo a abrir.
        #Modo de apertura del archivo ('r', 'w')

        self.file_name = file_name
        self.mode = mode
        try:
            self.file = open(file_name, mode)
            print(f"Archivo '{file_name}' abierto en modo '{mode}'")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            self.file = None

    def write_data(self, data):#escribir datos en el archivo

        if self.file and not self.file.closed:
            self.file.write(data)
            print(f"Datos escritos en el archivo '{self.file_name}'.")
        else:
            print("El archivo no está disponible para escribir.")

    def __del__(self):#cierra el archivo si esta abierto

        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo '{self.file_name}' cerrado correctamente.")

# Ejemplo de uso de la clase DocManager
def main():
    # Crear un objeto
    handler = DocManager("example.txt", "w")

    # Escribir datos en el archivo
    handler.write_data("Hola, este es un ejemplo de uso de constructores y destructores en Python.\n")

    # Dejar que el destructor cierre el archivo automáticamente al final del programa

if __name__ == "__main__":
    main()