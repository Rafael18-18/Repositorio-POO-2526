import tkinter as tk
from tkinter import ttk, messagebox

# ================= FUNCIONES =================

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")

def eliminar_evento():
    seleccion = tree.selection()
    if seleccion:
        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
        if confirmar:
            tree.delete(seleccion)
    else:
        messagebox.showwarning("Error", "Selecciona un evento")

# ================= VENTANA =================

root = tk.Tk()
root.title("Gestor de Eventos")
root.geometry("600x400")

# ================= FRAME LISTA =================

frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripcion"), show="headings")

tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripcion", text="Descripción")

tree.column("Fecha", width=100)
tree.column("Hora", width=100)
tree.column("Descripcion", width=250)

tree.pack()

# ================= FRAME ENTRADAS =================

frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_desc = tk.Entry(frame_entrada)
entry_desc.grid(row=2, column=1, padx=5, pady=5)

# ================= FRAME BOTONES =================

frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=10)

# ================= EJECUCIÓN =================

root.mainloop()