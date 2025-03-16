import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Semana 13")
root.geometry("400x500")
root.config(bg="#0A192F")
root.resizable(True, True)

# Variables de estado
texto_placeholder = "Ingrese su nota aquí"
texto_ingresado = False

def limpiar_placeholder(event=None):
    global texto_ingresado
    if not texto_ingresado:
        text_area.delete("1.0", tk.END)
        text_area.config(fg="white")
        texto_ingresado = True

def restaurar_placeholder(event=None):
    global texto_ingresado
    if text_area.get("1.0", tk.END).strip() == "":
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", texto_placeholder)
        text_area.config(fg="#7289A6")
        texto_ingresado = False

def on_key_press(event=None):
    global texto_ingresado
    if not texto_ingresado:
        text_area.delete("1.0", tk.END)
        text_area.config(fg="white")
        texto_ingresado = True

def agregar_texto(event=None):
    global texto_ingresado
    texto = text_area.get("1.0", tk.END).strip()
    if texto and texto != texto_placeholder:
        listbox.insert(0, texto)  # Insertar al inicio para mostrar las más recientes primero
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", texto_placeholder)  # Mostrar el placeholder después de agregar
        text_area.config(fg="#7289A6")
        texto_ingresado = False
    text_area.focus_set()
    if event:  # Si fue llamado por el evento Enter
        return "break"  # Evita el salto de línea en el TextArea

def limpiar_lista():
    if listbox.size() > 0:
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar todas las notas?"):
            listbox.delete(0, tk.END)
    listbox.focus_set()

def on_enter_boton(e, boton, color):
    boton.config(bg=color)

def on_leave_boton(e, boton, color):
    boton.config(bg=color)

# Estilo de fuente
fuente_sf = ("Segoe UI", 11)
fuente_botones = ("Segoe UI", 10, "bold")

# Frame principal con padding
main_frame = tk.Frame(root, bg="#0A192F", padx=15, pady=10)
main_frame.pack(fill="both", expand=True)

# TextArea con placeholder
text_area = tk.Text(main_frame, height=4, width=40, font=fuente_sf, bg="#112240", fg="#7289A6", 
                   insertbackground="white", padx=8, pady=8, wrap=tk.WORD)
text_area.insert("1.0", texto_placeholder)
text_area.bind("<FocusIn>", limpiar_placeholder)
text_area.bind("<FocusOut>", restaurar_placeholder)
text_area.bind("<Key>", on_key_press)
text_area.bind("<Return>", agregar_texto)
text_area.pack(fill="x", pady=(0, 10))

# Frame para los botones
frame_botones = tk.Frame(main_frame, bg="#0A192F")
frame_botones.pack(fill="x", pady=(0, 10))

# Botones
boton_agregar = tk.Button(frame_botones, text="Agregar", bg="#1E3A5F", fg="white", 
                         font=fuente_botones, padx=12, pady=4, cursor="hand2",
                         command=lambda: agregar_texto())
boton_agregar.pack(side="left", padx=(0, 5))

boton_limpiar = tk.Button(frame_botones, text="Limpiar", bg="#8B0000", fg="white", 
                         font=fuente_botones, padx=12, pady=4, cursor="hand2",
                         command=limpiar_lista)
boton_limpiar.pack(side="left", padx=(5, 0))

# Eventos de hover para los botones
boton_agregar.bind("<Enter>", lambda e: on_enter_boton(e, boton_agregar, "#2C4A7A"))
boton_agregar.bind("<Leave>", lambda e: on_leave_boton(e, boton_agregar, "#1E3A5F"))
boton_limpiar.bind("<Enter>", lambda e: on_enter_boton(e, boton_limpiar, "#B22222"))
boton_limpiar.bind("<Leave>", lambda e: on_leave_boton(e, boton_limpiar, "#8B0000"))

# Frame para el Listbox y Scrollbar
frame_lista = tk.Frame(main_frame, bg="#0A192F")
frame_lista.pack(fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

# Listbox con scrollbar
listbox = tk.Listbox(frame_lista, font=fuente_sf, bg="#1E3A5F", fg="white", 
                     selectbackground="#4C9EEB", selectmode=tk.SINGLE,
                     yscrollcommand=scrollbar.set)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox.yview)

# Foco inicial en el listbox
listbox.focus_set()

# Iniciar el bucle principal
root.mainloop()
