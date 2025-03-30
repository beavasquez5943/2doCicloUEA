import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingrese una tarea.")

def mark_completed():
    try:
        selected_index = tasks_listbox.curselection()[0]
        task_text = tasks_listbox.get(selected_index)
        tasks_listbox.delete(selected_index)
        tasks_listbox.insert(selected_index, f"✔ {task_text}")
    except IndexError:
        messagebox.showwarning("Selección Inválida", "Por favor, seleccione una tarea para marcar como completada.")

def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selección Inválida", "Por favor, seleccione una tarea para eliminar.")

def add_task_enter(event):
    add_task()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada y botón para añadir tarea
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task_enter)

add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack()

# Listbox para mostrar las tareas
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=10)

# Botones para completar y eliminar tareas
complete_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
complete_button.pack()

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack()

# Ejecutar la aplicación
root.mainloop()
