# Programa que demuestra los conceptos de Programación Orientada a Objetos
# Autor: Ignacio Rafael Vélez Ruiz

# Clase base
class Empleado:
    def __init__(self, nombre, salario):
        # Encapsulación: atributo privado
        self.__salario = salario
        self.nombre = nombre

    # Método para obtener el salario (getter)
    def get_salario(self):
        return self.__salario

    # Método para modificar el salario (setter)
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario

    # Método que será sobrescrito (polimorfismo)
    def calcular_salario(self):
        return self.__salario


# Clase derivada (Herencia)
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    # Polimorfismo: sobrescritura del método
    def calcular_salario(self):
        return self.get_salario() + self.bono


# Programa principal
if __name__ == "__main__":
    # Creación de objetos
    empleado1 = Empleado("Rafael", 500)
    empleado2 = EmpleadoTiempoCompleto("Ana", 800, 200)

    # Uso de métodos
    print("Empleado Base:")
    print("Nombre:", empleado1.nombre)
    print("Salario:", empleado1.calcular_salario())

    print("\nEmpleado Tiempo Completo:")
    print("Nombre:", empleado2.nombre)
    print("Salario Total:", empleado2.calcular_salario())
