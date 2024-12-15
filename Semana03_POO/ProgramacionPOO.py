class Clima:
    #atributos de la clase
    def __init__(self):
        self.temperaturas = []  #temperaturas diarias

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):  #7 temperaturas diarias
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        suma_temperaturas = sum(self.temperaturas)
        promedio = suma_temperaturas / len(self.temperaturas)
        return promedio


# HERENCIA
class ClimaConHistorial(Clima):
    def __init__(self, historial=None):
        super().__init__()
        self.historial = historial if historial else []  # Historial de promedios de semanas anteriores

    def agregar_historial(self, promedio):
        self.historial.append(promedio)

    def mostrar_historial(self):
        print("Historial de promedios semanales:")
        for i, promedio in enumerate(self.historial, 1):
            print(f"Semana {i}: {promedio:.2f}°C")


# Función principal
def main():
    clima = ClimaConHistorial()  # instancia de la herencia
    clima.ingresar_temperaturas()  # Ingresar las temperaturas diarias

    #promedio semanal
    promedio_semanal = clima.calcular_promedio()

    #resultado
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}°C")

    #historial
    clima.agregar_historial(promedio_semanal)

    # Mostrar historial
    clima.mostrar_historial()



if __name__ == "__main__":
    main()
