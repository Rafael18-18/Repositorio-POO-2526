from inventario import Inventario
from producto import Producto


def menu():
    inventario = Inventario()

    while True:
        print("\n====== SISTEMA DE GESTIÓN DE INVENTARIOS ======")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)

            except ValueError:
                print("Error: Debe ingresar valores numéricos válidos.")

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")

            try:
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)

            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\nResultados encontrados:")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
