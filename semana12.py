class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        # Uso tupla para datos que no van a cambiar (inmutables)
        self.datos = (isbn, titulo, autor)
        self.categoria = categoria
        self.disponible = True  # Añado un atributo para controlar disponibilidad
    
    def obtener_isbn(self):
        return self.datos[0]
    
    def obtener_titulo(self):
        return self.datos[1]
    
    def obtener_autor(self):
        return self.datos[2]
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ISBN: {self.datos[0]} | Título: {self.datos[1]} | Autor: {self.datos[2]} | Categoría: {self.categoria} | Estado: {estado}"


class Usuario:
    def __init__(self, id_usuario, nombre, email=None):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        # Lista para los libros que tiene el usuario actualmente
        self.libros_actuales = []
    
    def tomar_prestado(self, libro):
        if libro.disponible:
            self.libros_actuales.append(libro)
            libro.disponible = False
            return True
        return False
    
    def devolver(self, isbn):
        for i, libro in enumerate(self.libros_actuales):
            if libro.obtener_isbn() == isbn:
                libro.disponible = True
                return self.libros_actuales.pop(i)
        return None
    
    def listar_prestamos(self):
        return [f"{libro.obtener_titulo()} ({libro.obtener_isbn()})" for libro in self.libros_actuales]
    
    def __str__(self):
        prestamos = ", ".join(self.listar_prestamos()) if self.libros_actuales else "Ninguno"
        return f"ID: {self.id} | Nombre: {self.nombre} | Libros: {prestamos}"


class BibliotecaDigital:
    def __init__(self, nombre="Mi Biblioteca"):
        self.nombre = nombre
        # Diccionario para guardar y buscar libros rápido por ISBN
        self.catalogo = {}
        # Diccionario para gestionar usuarios por ID
        self.miembros = {}
        # Historial de préstamos como lista de tuplas (id_usuario, isbn, fecha)
        self.historial = []
        # Conjunto para categorías disponibles
        self.categorias = set()
    
    def agregar_libro(self, libro):
        isbn = libro.obtener_isbn()
        if isbn not in self.catalogo:
            self.catalogo[isbn] = libro
            self.categorias.add(libro.categoria)
            return True
        return False
    
    def quitar_libro(self, isbn):
        if isbn in self.catalogo:
            libro = self.catalogo.pop(isbn)
            # Verifico si quedan libros de esta categoría
            categoria_existe = False
            for l in self.catalogo.values():
                if l.categoria == libro.categoria:
                    categoria_existe = True
                    break
            if not categoria_existe:
                self.categorias.remove(libro.categoria)
            return libro
        return None
    
    def registrar_usuario(self, usuario):
        if usuario.id not in self.miembros:
            self.miembros[usuario.id] = usuario
            return True
        return False
    
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.miembros:
            # Verificar que no tenga préstamos pendientes
            usuario = self.miembros[id_usuario]
            if not usuario.libros_actuales:
                return self.miembros.pop(id_usuario)
        return None
    
    def prestar(self, id_usuario, isbn):
        from datetime import datetime
        
        if id_usuario in self.miembros and isbn in self.catalogo:
            usuario = self.miembros[id_usuario]
            libro = self.catalogo[isbn]
            
            if usuario.tomar_prestado(libro):
                # Registro el préstamo con fecha actual
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
                self.historial.append((id_usuario, isbn, fecha))
                return True
        return False
    
    def recibir(self, id_usuario, isbn):
        if id_usuario in self.miembros:
            usuario = self.miembros[id_usuario]
            libro_devuelto = usuario.devolver(isbn)
            if libro_devuelto:
                return True
        return False
    
    def buscar_por_titulo(self, texto):
        resultados = []
        for libro in self.catalogo.values():
            if texto.lower() in libro.obtener_titulo().lower():
                resultados.append(libro)
        return resultados
    
    def buscar_por_autor(self, autor):
        return [libro for libro in self.catalogo.values() 
                if autor.lower() in libro.obtener_autor().lower()]
    
    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.catalogo.values() 
                if libro.categoria.lower() == categoria.lower()]
    
    def mostrar_catalogo(self):
        print(f"=== CATÁLOGO DE {self.nombre.upper()} ===")
        if not self.catalogo:
            print("No hay libros en el catálogo.")
            return
        
        for libro in self.catalogo.values():
            print(libro)


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Creo mi biblioteca
    biblio = BibliotecaDigital("Biblioteca Municipal")
    
    # Agrego algunos libros
    libros = [
        Libro("978-84-376-0494-7", "Cien años de soledad", "Gabriel García Márquez", "Ficción"),
        Libro("978-0-7475-3269-9", "Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía"),
        Libro("978-84-339-7122-7", "1984", "George Orwell", "Ciencia Ficción"),
        Libro("978-84-376-0494-8", "El amor en los tiempos del cólera", "Gabriel García Márquez", "Ficción")
    ]
    
    for libro in libros:
        biblio.agregar_libro(libro)
    
    # Agrego algunos usuarios
    usuarios = [
        Usuario("U001", "María López", "maria@email.com"),
        Usuario("U002", "Carlos Rodríguez", "carlos@email.com")
    ]
    
    for usuario in usuarios:
        biblio.registrar_usuario(usuario)
    
    # Realizo algunas operaciones
    print("\n--- Catálogo inicial ---")
    biblio.mostrar_catalogo()
    
    print("\n--- Préstamo de libros ---")
    if biblio.prestar("U001", "978-84-376-0494-7"):
        print("Préstamo exitoso a María")
    
    if biblio.prestar("U002", "978-0-7475-3269-9"):
        print("Préstamo exitoso a Carlos")
    
    print("\n--- Estado de usuarios ---")
    for usuario in biblio.miembros.values():
        print(usuario)
    
    print("\n--- Catálogo actualizado ---")
    biblio.mostrar_catalogo()
    
    print("\n--- Búsqueda por autor 'García Márquez' ---")
    resultados = biblio.buscar_por_autor("García Márquez")
    for libro in resultados:
        print(libro)
    
    print("\n--- Devolución de libro ---")
    if biblio.recibir("U001", "978-84-376-0494-7"):
        print("Devolución exitosa de María")
    
    print("\n--- Estado final de usuarios ---")
    for usuario in biblio.miembros.values():
        print(usuario)