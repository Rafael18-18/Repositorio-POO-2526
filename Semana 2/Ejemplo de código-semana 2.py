
# Programa principal
cuadrado = Cuadrado(5)
circulo = Circulo(3)

print("Área del cuadrado:", cuadrado.area())
print("Área del círculo:", circulo.area())

from abc import ABC, abstractmethod
import math

# Clase abstracta que define qué debe hacer una figura
class Figura(ABC):

    @abstractmethod
    def area(self):
        """Método abstracto que todas las figuras deben implementar"""
        pass

# Clase que representa un cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

# Clase que representa un círculo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio


