import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.simpledialog
from datetime import datetime

# Ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Lista de eventos (fecha, hora, descripción)
eventos = []

# Agregar un evento
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Entrada incompleta", "Por favor complete todos los campos.")
        return

    # Agregar evento a la lista
    eventos.append((fecha, hora, descripcion))
    actualizar_lista()

    # Limpiar los campos de entrada
    fecha_entry.delete(0, tk.END)
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccion = lista_eventos.selection()
    if not seleccion:
        messagebox.showwarning("No seleccionado", "Por favor seleccione un evento para eliminar.")
        return

    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este evento?")
    if respuesta:
        for item in seleccion:
            # Eliminar el evento de la lista
            index = lista_eventos.index(item)
            del eventos[index]
        actualizar_lista()

# Función para actualizar la lista de eventos
def actualizar_lista():
    # Limpiar la lista de eventos
    for item in lista_eventos.get_children():
        lista_eventos.delete(item)

    # Agregar eventos a la lista
    for evento in eventos:
        lista_eventos.insert("", tk.END, values=evento)

# Interfaz de usuario
frame_lista = tk.Frame(root)
frame_lista.pack(padx=10, pady=10)

# Crear lista de eventos
lista_eventos = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
lista_eventos.heading("Fecha", text="Fecha")
lista_eventos.heading("Hora", text="Hora")
lista_eventos.heading("Descripción", text="Descripción")
lista_eventos.pack()

frame_entrada = tk.Frame(root)
frame_entrada.pack(padx=10, pady=10)

# Etiquetas y campos de entrada
tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0)
fecha_entry = tk.Entry(frame_entrada)
fecha_entry.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0)
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
descripcion_entry = tk.Entry(frame_entrada)
descripcion_entry.grid(row=2, column=1)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(padx=10, pady=10)

boton_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=0, column=0, padx=5)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.grid(row=0, column=1, padx=5)

boton_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
boton_salir.grid(row=0, column=2, padx=5)

# Iniciar la aplicación
root.mainloop()