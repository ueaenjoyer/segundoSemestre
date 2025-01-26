class FileHandler:
    """
    Clase que simula la apertura y cierre de un archivo.
    Demuestra el uso de constructores (__init__) y destructores (__del__).
    """

    def __init__(self, filename):
        """
        Constructor que inicializa el nombre del archivo y simula la apertura del archivo.
        :param filename: Nombre del archivo a manejar.
        """
        self.filename = filename
        print(f"[INFO] Inicializando el manejador para el archivo: {self.filename}")
        self.file = None  # Atributo para almacenar el estado del archivo
        self.open_file()

    def open_file(self):
        """
        Método que simula la apertura del archivo.
        """
        self.file = f"Archivo '{self.filename}' abierto con éxito."
        print(self.file)

    def read_file(self):
        """
        Método que simula la lectura del archivo.
        """
        if self.file:
            print(f"Leyendo contenido de {self.filename}...")
            return f"Contenido simulado de {self.filename}."
        else:
            print("El archivo no está abierto.")
            return None

    def __del__(self):
        """
        Destructor que cierra el archivo (si está abierto) y libera recursos.
        """
        if self.file:
            print(f"[INFO] Cerrando el archivo: {self.filename}")
            self.file = None  # Simula el cierre del archivo
        print(f"[INFO] El manejador para {self.filename} ha sido destruido.")


# Ejemplo de uso
print("Creando un objeto FileHandler...")
handler = FileHandler("mi_archivo.txt")  # Llama al constructor (__init__)

print("\nLeyendo el archivo...")
contenido = handler.read_file()
print(f"Contenido leído: {contenido}")

print("\nEliminando el objeto...")
del handler  # Llama al destructor (__del__)

print("\nPrograma terminado.")
