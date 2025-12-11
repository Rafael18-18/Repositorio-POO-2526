# ----------------------------------------------
# Programa: Promedio semanal de temperaturas
# Programación Orientada a Objetos (POO)
# ----------------------------------------------

class ClimaSemanal:
    def __init__(self):
        # Atributo encapsulado (privado)
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método que solicita las temperaturas de los 7 días.
        """
        print("Ingrese las temperaturas diarias:")

        for i in range(7):
            temp = float(input(f" Día {i+1}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio de las temperaturas almacenadas.
        """
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)


# Ejemplo de uso
def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()
