# ================================
# CLASE LIBRO
# ================================
# Representa un libro dentro de la biblioteca

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para guardar título y autor porque no cambian
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    # Método para mostrar la información del libro
    def mostrar(self):
        return f"Titulo: {self.info[0]}, Autor: {self.info[1]}, Categoria: {self.categoria}, ISBN: {self.isbn}"


# ================================
# CLASE USUARIO
# ================================
# Representa un usuario registrado en la biblioteca

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para guardar los libros que tiene prestados
        self.libros_prestados = []

    # Mostrar libros prestados
    def mostrar_libros(self):
        for libro in self.libros_prestados:
            print(libro.mostrar())


# ================================
# CLASE BIBLIOTECA
# ================================
# Gestiona libros, usuarios y préstamos

class Biblioteca:
    def __init__(self):
        # Diccionario para guardar libros (ISBN como clave)
        self.libros = {}

        # Diccionario para guardar usuarios
        self.usuarios = {}

        # Conjunto para garantizar IDs únicos
        self.ids_usuarios = set()

    # ================================
    # AÑADIR LIBRO
    # ================================
    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro agregado correctamente")

    # ================================
    # QUITAR LIBRO
    # ================================
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # ================================
    # REGISTRAR USUARIO
    # ================================
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente")
        else:
            print("El ID de usuario ya existe")

    # ================================
    # DAR DE BAJA USUARIO
    # ================================
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # ================================
    # PRESTAR LIBRO
    # ================================
    def prestar_libro(self, id_usuario, isbn):

        if id_usuario in self.usuarios and isbn in self.libros:

            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]

            usuario.libros_prestados.append(libro)
            del self.libros[isbn]

            print("Libro prestado correctamente")

        else:
            print("No se pudo realizar el préstamo")

    # ================================
    # DEVOLVER LIBRO
    # ================================
    def devolver_libro(self, id_usuario, isbn):

        if id_usuario in self.usuarios:

            usuario = self.usuarios[id_usuario]

            for libro in usuario.libros_prestados:

                if libro.isbn == isbn:

                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro

                    print("Libro devuelto correctamente")
                    return

        print("No se encontró el libro")

    # ================================
    # BUSCAR LIBRO
    # ================================
    def buscar_libro(self, texto):

        print("Resultados de búsqueda:")

        for libro in self.libros.values():

            titulo = libro.info[0]
            autor = libro.info[1]

            if texto.lower() in titulo.lower() or texto.lower() in autor.lower() or texto.lower() in libro.categoria.lower():

                print(libro.mostrar())

    # ================================
    # LISTAR LIBROS PRESTADOS
    # ================================
    def listar_prestados(self, id_usuario):

        if id_usuario in self.usuarios:

            usuario = self.usuarios[id_usuario]

            print("Libros prestados a", usuario.nombre)

            for libro in usuario.libros_prestados:
                print(libro.mostrar())

        else:
            print("Usuario no encontrado")


# =================================
# PRUEBA DEL SISTEMA
# =================================

biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", "101")
libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Clasico", "102")
libro3 = Libro("Python Basico", "Juan Perez", "Programacion", "103")

# Añadir libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear usuario
usuario1 = Usuario("Ignacio", 1)

# Registrar usuario
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro(1, "101")

# Ver libros prestados
biblioteca.listar_prestados(1)

# Devolver libro
biblioteca.devolver_libro(1, "101")

# Buscar libro
biblioteca.buscar_libro("Python")