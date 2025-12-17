# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_datos(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula}"


# Clase que representa una reserva
class Reserva:
    def __init__(self, cliente, fecha, lugar):
        self.cliente = cliente
        self.fecha = fecha
        self.lugar = lugar

    def mostrar_reserva(self):
        return (
            f"Reserva a nombre de {self.cliente.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Lugar: {self.lugar}"
        )


# Programa principal
if __name__ == "__main__":
    # Crear un cliente
    cliente1 = Cliente("Ignacio Vélez", "0923456789")

    # Crear una reserva
    reserva1 = Reserva(cliente1, "28/12/2025", "Hotel Balzar")

    # Mostrar información
    print(cliente1.mostrar_datos())
    print("------------------------")
    print(reserva1.mostrar_reserva())
