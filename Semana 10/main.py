import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_line(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_line(linea):
        try:
            codigo, nombre, cantidad, precio = linea.strip().split(",")
            return Producto(codigo, nombre, int(cantidad), float(precio))
        except ValueError:
            # Si el archivo está corrupto
            print("⚠ Línea inválida detectada en el archivo y será ignorada.")
            return None


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    # ==============================
    # CARGAR INVENTARIO
    # ==============================
    def cargar_inventario(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                print("📁 Archivo creado automáticamente.\n")

            with open(self.archivo, "r") as f:
                for linea in f:
                    producto = Producto.from_line(linea)
                    if producto:
                        self.productos[producto.codigo] = producto

            print("✅ Inventario cargado correctamente.\n")

        except PermissionError:
            print("❌ Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print("❌ Error inesperado al cargar:", e)

    # ==============================
    # GUARDAR INVENTARIO
    # ==============================
    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(producto.to_line() + "\n")
            print("💾 Cambios guardados correctamente.\n")
        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print("❌ Error inesperado al guardar:", e)

    # ==============================
    # AGREGAR PRODUCTO
    # ==============================
    def agregar_producto(self):
        codigo = input("Código: ")

        if codigo in self.productos:
            print("⚠ El producto ya existe.\n")
            return

        nombre = input("Nombre: ")

        try:
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
        except ValueError:
            print("❌ Error: Cantidad y precio deben ser números.\n")
            return

        self.productos[codigo] = Producto(codigo, nombre, cantidad, precio)
        self.guardar_inventario()
        print("✅ Producto agregado exitosamente.\n")

    # ==============================
    # ELIMINAR PRODUCTO
    # ==============================
    def eliminar_producto(self):
        codigo = input("Código del producto a eliminar: ")

        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print("🗑 Producto eliminado correctamente.\n")
        else:
            print("❌ Producto no encontrado.\n")

    # ==============================
    # ACTUALIZAR PRODUCTO
    # ==============================
    def actualizar_producto(self):
        codigo = input("Código del producto a actualizar: ")

        if codigo not in self.productos:
            print("❌ Producto no encontrado.\n")
            return

        try:
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
        except ValueError:
            print("❌ Error: Datos inválidos.\n")
            return

        self.productos[codigo].cantidad = cantidad
        self.productos[codigo].precio = precio
        self.guardar_inventario()
        print("🔄 Producto actualizado correctamente.\n")

    # ==============================
    # MOSTRAR PRODUCTOS
    # ==============================
    def mostrar_productos(self):
        if not self.productos:
            print("📭 Inventario vacío.\n")
            return

        print("\n===== INVENTARIO ACTUAL =====")
        for p in self.productos.values():
            print(f"Código: {p.codigo}")
            print(f"Nombre: {p.nombre}")
            print(f"Cantidad: {p.cantidad}")
            print(f"Precio: {p.precio}")
            print("---------------------------")


# ==============================
# MENÚ PRINCIPAL
# ==============================
def menu():
    inventario = Inventario()

    while True:
        print("===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.agregar_producto()
        elif opcion == "2":
            inventario.eliminar_producto()
        elif opcion == "3":
            inventario.actualizar_producto()
        elif opcion == "4":
            inventario.mostrar_productos()
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.\n")


if __name__ == "__main__":
    menu()
