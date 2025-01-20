class Empleado: #clase base empleado generico
    def __init__(self, nombre, salario_base): #atributos empleados
        self._nombre = nombre  # Atributo protegido/nombre
        self._salario_base = salario_base  # Atributo protegido/salario

    def calcular_salario(self): #salario base/polimorfismo

        return self._salario_base

    def descripcion(self): #descripcion empleado
        return f"Empleado: {self._nombre}, Salario Base: {self._salario_base}"


class Gerente(Empleado): #clase gerente/clase empleado
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)  #constructor clase base: nomb/salario
        self.__bono = bono  #bono especifico

    def calcular_salario(self):#polimorfismo/salario + bono
        return self._salario_base + self.__bono

    def descripcion(self):#descripcion generente:nomb+salario+bono
        return f"Gerente: {self._nombre}, Salario Total: {self.calcular_salario()}"

    # Encapsulación: Métodos para acceder y modificar el bono
    def get_bono(self):
        return self.__bono

    def set_bono(self, bono):
        if bono > 0:#bono positivo al salario
            self.__bono = bono
        else:
            print("El bono debe ser mayor que 0.")


class Interno(Empleado): #clase interno/clase empleado
    def __init__(self, nombre, salario_base, horas_extras):#horas extras
        super().__init__(nombre, salario_base)
        self.horas_extras = horas_extras  # Atributo público

    def calcular_salario(self): #salario base mas extras

        salario_horas_extras = self.horas_extras * 50  #tarifa horas extras
        return self._salario_base + salario_horas_extras

    def descripcion(self): #salario total total
        return f"Interno: {self._nombre}, Salario Total: {self.calcular_salario()}"


if __name__ == "__main__":
    # Instancia de la clase base Empleado
    empleado1 = Empleado("Carlos", 3000)
    print(empleado1.descripcion())

    # Instancia de la clase derivada Gerente
    gerente1 = Gerente("María", 5000, 2000)
    print(gerente1.descripcion())

    # Uso de encapsulación para acceder y modificar el bono
    print("Bono actual del gerente:", gerente1.get_bono())
    gerente1.set_bono(2500)
    print("Bono actualizado del gerente:", gerente1.get_bono())

    # Instancia de la clase derivada Interno
    interno1 = Interno("Luis", 1500, 10)
    print(interno1.descripcion())


    empleados = [empleado1, gerente1, interno1]
    for empleado in empleados:
        print(f"{empleado.descripcion()} - Salario Calculado: {empleado.calcular_salario()}")
