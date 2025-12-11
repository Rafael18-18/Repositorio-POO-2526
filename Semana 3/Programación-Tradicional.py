# -----------------------------
# Programa: Promedio semanal de temperaturas
# Programación Tradicional
# -----------------------------

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    print("Ingrese las temperaturas diarias:")

    for i in range(7):
        temp = float(input(f" Día {i+1}: "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio(temps):
    """
    Recibe una lista de temperaturas y retorna el promedio semanal.
    """
    return sum(temps) / len(temps)


# ------ Programa principal ------
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal es: {promedio:.2f} °C")


# Ejecutar
if __name__ == "__main__":
    main()
