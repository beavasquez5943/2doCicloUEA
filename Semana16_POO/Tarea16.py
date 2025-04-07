import tkinter as tk
from tkinter import messagebox

# Añadir tarea
def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

# Marcar tarea como completada
def mark_completed():
    try:
        selected_task_index = tasks_listbox.curselection()
        if selected_task_index:
            task = tasks_listbox.get(selected_task_index)
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, task + " (Completada)")
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al marcar la tarea como completada: {e}")

# Eliminar tarea
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()
        if selected_task_index:
            tasks_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar la tarea: {e}")

# Cerrar la aplicación
def close_app(event=None):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear el campo de entrada (Entry) para nuevas tareas
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=0, padx=10, pady=10)

# Crear la lista de tareas (Listbox)
tasks_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
tasks_listbox.grid(row=1, column=0, padx=10, pady=10)

# Crear botones para añadir, marcar como completada y eliminar tareas
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')

mark_button = tk.Button(root, text="Marcar Completada", command=mark_completed)
mark_button.grid(row=3, column=0, padx=10, pady=10, sticky='w')

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.grid(row=4, column=0, padx=10, pady=10, sticky='w')

# Configurar atajos de teclado
root.bind('<Return>', lambda event: add_task())  # Enter para añadir tarea
root.bind('<c>', lambda event: mark_completed())  # 'C' para marcar completada
root.bind('<Delete>', lambda event: delete_task())  # 'Delete' para eliminar tarea
root.bind('<d>', lambda event: delete_task())  # 'D' para eliminar tarea
root.bind('<Escape>', close_app)  # Escape para cerrar la aplicación

# Iniciar la aplicación
root.mainloop()