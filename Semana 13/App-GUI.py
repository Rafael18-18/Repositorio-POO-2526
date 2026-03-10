import tkinter as tk


# Función para agregar datos
def agregar_dato():
    texto = entrada.get()

    if texto != "":
        lista_datos.insert(tk.END, texto)
        entrada.delete(0, tk.END)


# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos - Aplicación GUI")
ventana.geometry("400x300")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=10)

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()