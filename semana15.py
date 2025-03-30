import tkinter as tk
from tkinter import messagebox
from tkinter import font  # Importar el módulo font

# --- Funciones Lógicas ---

def add_task(event=None):
    """Añade una nueva tarea a la lista."""
    task = task_entry.get()  # Obtener el texto del campo de entrada
    if task != "":
        # Verificar si la tarea ya tiene un marcador de completada (para evitar duplicados visuales)
        if not task.startswith("✓ "):
             tasks_listbox.insert(tk.END, task) # Insertar la tarea al final de la lista
             task_entry.delete(0, tk.END) # Limpiar el campo de entrada después de añadir
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea que ya está marcada como completada.")
            task_entry.delete(0, tk.END) # Limpiar también si es inválida
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

def mark_complete(event=None):
    """Marca la tarea seleccionada como completada."""
    try:
        selected_task_index = tasks_listbox.curselection()[0] # Obtener índice de la tarea seleccionada
        task_text = tasks_listbox.get(selected_task_index) # Obtener el texto de la tarea

        # Verificar si ya está completada para no añadir múltiples marcas
        if not task_text.startswith("✓ "):
            completed_task_text = f"✓ {task_text}"
            # Eliminar la tarea original
            tasks_listbox.delete(selected_task_index)
            # Insertar la tarea marcada como completada en la misma posición (o al final si prefieres)
            tasks_listbox.insert(selected_task_index, completed_task_text)
            # Cambiar el color y estilo de la tarea completada
            tasks_listbox.itemconfig(selected_task_index, {'fg': 'gray'}) # Poner texto en gris

        # Deseleccionar después de marcar para evitar acciones accidentales
        tasks_listbox.selection_clear(0, tk.END)

    except IndexError:
        # Esto ocurre si no se selecciona ninguna tarea
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para marcarla como completada.")

def delete_task():
    """Elimina la tarea seleccionada de la lista."""
    try:
        selected_task_index = tasks_listbox.curselection()[0] # Obtener índice de la tarea seleccionada
        tasks_listbox.delete(selected_task_index) # Eliminar la tarea de la lista
    except IndexError:
        # Esto ocurre si no se selecciona ninguna tarea
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminarla.")

# --- Configuración de la Interfaz Gráfica ---

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Simple")
root.geometry("400x450") # Tamaño inicial de la ventana (ancho x alto)
root.configure(bg="#f0f0f0") # Color de fondo general

# Crear un Frame principal para organizar mejor los widgets
main_frame = tk.Frame(root, bg="#f0f0f0")
# Usar pack con fill=tk.BOTH y expand=True para que el frame ocupe toda la ventana
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Título dentro de la ventana
title_label = tk.Label(main_frame, text="Lista de Tareas", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=(0, 10)) # Espacio vertical debajo del título

# --- Widgets de Entrada y Botón de Añadir ---

# Frame para la entrada y el botón de añadir
add_frame = tk.Frame(main_frame, bg="#f0f0f0")
add_frame.pack(fill=tk.X) # Ocupar el ancho disponible

# Campo de entrada para nuevas tareas
task_entry = tk.Entry(add_frame, width=30, font=("Arial", 12), bd=2, relief=tk.GROOVE)
# Usar pack para colocar la entrada a la izquierda, expandiéndose
task_entry.pack(side=tk.LEFT, padx=(0, 5), ipady=4, fill=tk.X, expand=True) # ipady para altura interna

# Botón para añadir tareas
add_button = tk.Button(add_frame, text="Añadir Tarea", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED, borderwidth=2, padx=5)
add_button.pack(side=tk.LEFT, ipady=1) # ipady para ajustar altura

# --- Lista de Tareas ---

# Frame para el Listbox y la barra de desplazamiento
list_frame = tk.Frame(main_frame)
# Añadir espacio vertical antes y después del list frame
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Listbox para mostrar las tareas
tasks_listbox = tk.Listbox(
    list_frame,
    width=50,
    height=10,
    font=("Arial", 12),
    bd=2,               # Borde
    relief=tk.GROOVE,   # Estilo del borde
    selectbackground="#a6a6a6", # Color de fondo del elemento seleccionado
    selectforeground="white",   # Color de texto del elemento seleccionado
    activestyle='none'  # Para evitar el subrayado al pasar el ratón si no se desea
)
# Usar pack para colocar el listbox a la izquierda y que se expanda verticalmente
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de desplazamiento para la lista
scrollbar_tasks = tk.Scrollbar(list_frame)
# Usar pack para colocar la barra a la derecha y que llene el espacio vertical
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar la barra de desplazamiento para controlar la vista del Listbox
tasks_listbox.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=tasks_listbox.yview)

# --- Botones de Acción (Marcar/Eliminar) ---

# Frame para los botones de acción inferiores
action_frame = tk.Frame(main_frame, bg="#f0f0f0")
action_frame.pack(fill=tk.X, pady=(5, 0)) # Espacio vertical arriba

# Botón para marcar como completada
mark_button = tk.Button(action_frame, text="Marcar como Completada", command=mark_complete, bg="#FFC107", fg="black", font=("Arial", 10, "bold"), relief=tk.RAISED, borderwidth=2, padx=5)
# Usar pack, expandiéndose para ocupar espacio horizontalmente
mark_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5), ipady=1)

# Botón para eliminar tarea
delete_button = tk.Button(action_frame, text="Eliminar Tarea", command=delete_task, bg="#f44336", fg="white", font=("Arial", 10, "bold"), relief=tk.RAISED, borderwidth=2, padx=5)
# Usar pack, expandiéndose para ocupar espacio horizontalmente
delete_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0), ipady=1)


# --- Vinculación de Eventos Adicionales ---

# Vincular la tecla Enter en el campo de entrada a la función add_task
task_entry.bind("<Return>", add_task)

# Opcional: Vincular doble clic en la lista a la función mark_complete
tasks_listbox.bind("<Double-Button-1>", mark_complete)

# --- Iniciar el Bucle Principal de la Aplicación ---
root.mainloop()