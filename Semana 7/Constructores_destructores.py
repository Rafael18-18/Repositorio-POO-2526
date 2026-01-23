# Clase que demuestra el uso de constructor y destructor en Python

class ArchivoLog:
    """
    Esta clase maneja un archivo de registro.
    El constructor abre el archivo.
    El destructor cierra el archivo cuando el objeto es eliminado.
    """

    def __init__(self, nombre_archivo):
        """
        CONSTRUCTOR
        Se ejecuta automáticamente cuando se crea un objeto de la clase.
        Inicializa los atributos y abre el archivo.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "a")
        print(f"[INFO] Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir_log(self, mensaje):
        """
        Método para escribir mensajes en el archivo de log.
        """
        self.archivo.write(mensaje + "\n")
        print(f"[LOG] {mensaje}")

    def __del__(self):
        """
        DESTRUCTOR
        Se ejecuta automáticamente cuando el objeto es destruido
        (por ejemplo, al finalizar el programa).
        Se usa para liberar recursos.
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"[INFO] Archivo '{self.nombre_archivo}' cerrado correctamente.")


# Programa principal
if __name__ == "__main__":
    # Creación del objeto (se ejecuta el constructor)
    log = ArchivoLog("registro.txt")

    # Uso del objeto
    log.escribir_log("Programa iniciado")
    log.escribir_log("Ejecutando tareas importantes")
    log.escribir_log("Programa finalizado")

    # Al terminar el programa, Python elimina el objeto
    # y se ejecuta automáticamente el destructor (__del__)
