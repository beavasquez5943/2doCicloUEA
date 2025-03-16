import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Función para agregar datos a la lista
def agregar_dato():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    fecha_inicio = entrada_fecha_inicio.get()
    fecha_fin = entrada_fecha_fin.get()
    comentario = entrada_comentario.get("1.0", tk.END).strip()

    if usuario and contrasena and fecha_inicio and fecha_fin and comentario:
        lista_datos.insert(tk.END,
                           f"Usuario: {usuario}, Fecha Inicio: {fecha_inicio}, Fecha Fin: {fecha_fin}, Comentario: {comentario}")
        entrada_usuario.delete(0, tk.END)
        entrada_contrasena.delete(0, tk.END)
        entrada_fecha_inicio.delete(0, tk.END)
        entrada_fecha_fin.delete(0, tk.END)
        entrada_comentario.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")


# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Actividad - MTT 2025")
ventana.geometry("500x400")

# Etiquetas y campos de entrada
etiqueta_usuario = tk.Label(ventana, text="Usuario:")
etiqueta_usuario.pack(pady=2)
entrada_usuario = tk.Entry(ventana, width=40)
entrada_usuario.pack(pady=2)

etiqueta_contrasena = tk.Label(ventana, text="Contraseña:")
etiqueta_contrasena.pack(pady=2)
entrada_contrasena = tk.Entry(ventana, width=40, show="*")
entrada_contrasena.pack(pady=2)

etiqueta_fecha_inicio = tk.Label(ventana, text="Fecha de inicio:")
etiqueta_fecha_inicio.pack(pady=2)
entrada_fecha_inicio = tk.Entry(ventana, width=40)
entrada_fecha_inicio.pack(pady=2)

etiqueta_fecha_fin = tk.Label(ventana, text="Fecha de fin:")
etiqueta_fecha_fin.pack(pady=2)
entrada_fecha_fin = tk.Entry(ventana, width=40)
entrada_fecha_fin.pack(pady=2)

etiqueta_comentario = tk.Label(ventana, text="Comentario:")
etiqueta_comentario.pack(pady=2)
entrada_comentario = tk.Text(ventana, width=40, height=5)
entrada_comentario.pack(pady=2)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=60, height=10)
lista_datos.pack(pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()