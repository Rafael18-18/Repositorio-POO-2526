import tkinter as tk
from tkinter import messagebox

# Lista para guardar tareas (texto, estado)
tareas = []


def añadir_tarea(event=None):
    tarea = entry.get().strip()
    if tarea == "":
        messagebox.showwarning("Aviso", "Escribe una tarea")
        return

    tareas.append((tarea, False))  # False = pendiente
    entry.delete(0, tk.END)
    actualizar_lista()


def marcar_completada(event=None):
    try:
        indice = lista.curselection()[0]
        texto, estado = tareas[indice]
        tareas[indice] = (texto, True)
        actualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Selecciona una tarea")


def eliminar_tarea(event=None):
    try:
        indice = lista.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Selecciona una tarea")


def actualizar_lista():
    lista.delete(0, tk.END)
    for i, (texto, estado) in enumerate(tareas):
        if estado:
            lista.insert(tk.END, "✔ " + texto)
            lista.itemconfig(i, fg="gray")
        else:
            lista.insert(tk.END, texto)
            lista.itemconfig(i, fg="black")


# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Entrada
entry = tk.Entry(ventana, font=("Arial", 12))
entry.pack(pady=10, padx=10, fill=tk.X)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_añadir = tk.Button(frame_botones, text="Añadir", command=añadir_tarea)
btn_añadir.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Completar", command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
lista = tk.Listbox(ventana, font=("Arial", 12))
lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Atajos de teclado
ventana.bind("<Return>", añadir_tarea)
ventana.bind("c", marcar_completada)
ventana.bind("C", marcar_completada)
ventana.bind("<Delete>", eliminar_tarea)
ventana.bind("d", eliminar_tarea)
ventana.bind("D", eliminar_tarea)
ventana.bind("<Escape>", lambda e: ventana.destroy())

# Ejecutar app
ventana.mainloop()