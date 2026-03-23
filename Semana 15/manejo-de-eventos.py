import tkinter as tk
from tkinter import ttk

# Crear ventana
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("500x400")
ventana.config(bg="#f0f0f0")

# Lista interna
tareas = []

# -------- FUNCIONES --------
def añadir_tarea(event=None):
    tarea = entrada.get().strip()
    if tarea != "":
        tree.insert("", "end", values=(tarea, "Pendiente"))
        tareas.append("Pendiente")
        entrada.delete(0, tk.END)

def marcar_completada():
    seleccion = tree.selection()
    if seleccion:
        item = seleccion[0]
        tree.item(item, values=(tree.item(item, "values")[0], "Completada"))

def eliminar_tarea():
    seleccion = tree.selection()
    if seleccion:
        item = seleccion[0]
        tree.delete(item)

def doble_click(event):
    marcar_completada()

# -------- INTERFAZ --------

# Entrada
entrada = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada.pack(pady=10)

entrada.bind("<Return>", añadir_tarea)

# Botones
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=5)

btn_add = tk.Button(frame_botones, text="Añadir Tarea", command=añadir_tarea, bg="#4CAF50", fg="white")
btn_add.grid(row=0, column=0, padx=5)

btn_done = tk.Button(frame_botones, text="Marcar Completada", command=marcar_completada, bg="#2196F3", fg="white")
btn_done.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea, bg="#f44336", fg="white")
btn_delete.grid(row=0, column=2, padx=5)

# Tabla (Treeview)
tree = ttk.Treeview(ventana, columns=("Tarea", "Estado"), show="headings")
tree.heading("Tarea", text="Tarea")
tree.heading("Estado", text="Estado")
tree.pack(pady=20, fill="both", expand=True)

# Evento doble clic
tree.bind("<Double-1>", doble_click)

# Ejecutar app
ventana.mainloop()