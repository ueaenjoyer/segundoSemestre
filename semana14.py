import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3
from tkcalendar import DateEntry

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Crear base de datos
        self.crear_base_datos()

        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame para entrada de datos
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Nuevo Evento", padding="10")
        self.input_frame.pack(fill=tk.X, pady=10)

        # Campos de entrada para fecha con DatePicker
        ttk.Label(self.input_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.input_frame, width=12, background='darkblue',
                                   foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy',
                                   firstweekday='sunday')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Frame para hora con spinboxes
        hora_frame = ttk.Frame(self.input_frame)
        hora_frame.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        ttk.Label(self.input_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        
        # Spinbox para horas (0-23)
        self.hora_spin = ttk.Spinbox(hora_frame, from_=0, to=23, width=2, format="%02.0f")
        self.hora_spin.set("12")
        self.hora_spin.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(hora_frame, text=":").pack(side=tk.LEFT)
        
        # Spinbox para minutos (0-59)
        self.min_spin = ttk.Spinbox(hora_frame, from_=0, to=59, width=2, format="%02.0f")
        self.min_spin.set("00")
        self.min_spin.pack(side=tk.LEFT, padx=2)

        # Campo para descripción
        ttk.Label(self.input_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.input_frame, width=40)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botón agregar
        self.btn_agregar = ttk.Button(self.input_frame, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame para la lista de eventos
        self.list_frame = ttk.LabelFrame(self.main_frame, text="Eventos Programados", padding="10")
        self.list_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.list_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar para el TreeView
        scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Frame para botones de acción
        self.action_frame = ttk.Frame(self.main_frame)
        self.action_frame.pack(fill=tk.X, pady=10)

        # Botones
        self.btn_eliminar = ttk.Button(self.action_frame, text="Eliminar Evento", command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)
        
        self.btn_salir = ttk.Button(self.action_frame, text="Salir", command=root.quit)
        self.btn_salir.pack(side=tk.RIGHT, padx=5)

        # Cargar eventos existentes
        self.cargar_eventos()

    def crear_base_datos(self):
        conn = sqlite3.connect('agenda.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS eventos
                    (fecha TEXT, hora TEXT, descripcion TEXT)''')
        conn.commit()
        conn.close()

    def validar_fecha(self, fecha):
        try:
            return datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            return None

    def obtener_hora(self):
        """Obtiene la hora actual de los spinboxes en formato HH:MM"""
        hora = self.hora_spin.get().zfill(2)
        minutos = self.min_spin.get().zfill(2)
        return f"{hora}:{minutos}"

    def agregar_evento(self):
        fecha = self.fecha_entry.get_date().strftime("%d/%m/%Y")
        hora = self.obtener_hora()
        descripcion = self.desc_entry.get()

        if not fecha or not descripcion:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return

        # Validar formato de hora
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Por favor seleccione una hora válida")
            return

        conn = sqlite3.connect('agenda.db')
        c = conn.cursor()
        c.execute("INSERT INTO eventos VALUES (?, ?, ?)", (fecha, hora, descripcion))
        conn.commit()
        conn.close()

        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
        self.desc_entry.delete(0, tk.END)
        self.fecha_entry.set_date(datetime.now())
        self.hora_spin.set("12")
        self.min_spin.set("00")
        messagebox.showinfo("Éxito", "Evento agregado correctamente")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un evento para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?"):
            valores = self.tree.item(seleccion)['values']
            conn = sqlite3.connect('agenda.db')
            c = conn.cursor()
            c.execute("DELETE FROM eventos WHERE fecha=? AND hora=? AND descripcion=?", valores)
            conn.commit()
            conn.close()
            self.tree.delete(seleccion)
            messagebox.showinfo("Éxito", "Evento eliminado correctamente")

    def cargar_eventos(self):
        conn = sqlite3.connect('agenda.db')
        c = conn.cursor()
        c.execute("SELECT * FROM eventos")
        eventos = c.fetchall()
        for evento in eventos:
            self.tree.insert("", tk.END, values=evento)
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()