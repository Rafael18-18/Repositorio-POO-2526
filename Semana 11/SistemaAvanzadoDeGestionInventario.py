import json

# ==========================
# CLASE PRODUCTO
# ==========================
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.__id = id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Convertir a diccionario (para guardar en JSON)
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }


# ==========================
# CLASE INVENTARIO
# ==========================
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario
        self.cargar_archivo()

    # Añadir producto
    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto
        self.guardar_archivo()

    # Eliminar producto
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_archivo()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
            self.guardar_archivo()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]
        for p in encontrados:
            print(p.to_dict())
        if not encontrados:
            print("No se encontraron productos.")

    # Mostrar todos
    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        for p in self.productos.values():
            print(p.to_dict())

    # Guardar en archivo
    def guardar_archivo(self):
        with open("inventario.json", "w") as archivo:
            datos = {id: p.to_dict() for id, p in self.productos.items()}
            json.dump(datos, archivo, indent=4)

    # Cargar desde archivo
    def cargar_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                for id, info in datos.items():
                    producto = Producto(
                        info["id"],
                        info["nombre"],
                        info["cantidad"],
                        info["precio"]
                    )
                    self.productos[id] = producto
        except FileNotFoundError:
            pass


# ==========================
# MENÚ INTERACTIVO
# ==========================
def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")


# Ejecutar programa
if __name__ == "__main__":
    menu()