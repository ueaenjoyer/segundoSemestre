class Producto:
    # Clase que representa un producto en el inventario
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre            # Nombre del producto
        self.cantidad = cantidad        # Cantidad disponible en inventario
        self.precio = precio            # Precio del producto

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    # Clase que gestiona el inventario de productos y su persistencia en archivo
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos con ID como clave
        self.archivo = "inventario.txt"
        self.cargar_inventario()  # Carga los productos existentes al iniciar

    def cargar_inventario(self):
        # Carga el inventario desde el archivo. Si el archivo no existe, se crea uno nuevo.
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue  # Salta líneas vacías
                    partes = linea.split(";")
                    if len(partes) == 4:
                        try:
                            id_producto = int(partes[0])
                            nombre = partes[1]
                            cantidad = int(partes[2])
                            precio = float(partes[3])
                            producto = Producto(id_producto, nombre, cantidad, precio)
                            self.productos[id_producto] = producto
                        except ValueError:
                            print(f"Error al convertir datos de la línea: {linea}")
        except FileNotFoundError:
            # Si el archivo no existe, se crea uno vacío
            with open(self.archivo, "w") as f:
                pass
            print("Archivo de inventario no encontrado. Se ha creado uno nuevo.")
        except PermissionError:
            print("Error: Permiso denegado para leer el archivo de inventario.")
        except Exception as e:
            print("Error inesperado al cargar el inventario:", e)

    def guardar_inventario(self) -> bool:
        # Guarda el inventario actual en el archivo
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    # Se escribe cada producto en una línea con formato: id;nombre;cantidad;precio
                    f.write(f"{producto.id_producto};{producto.nombre};{producto.cantidad};{producto.precio}\n")
            return True
        except FileNotFoundError:
            print("Error: Archivo de inventario no encontrado.")
            return False
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo de inventario.")
            return False
        except Exception as e:
            print("Error inesperado al guardar el inventario:", e)
            return False

    def obtener_siguiente_id(self) -> int:
        # Calcula el siguiente ID disponible basado en los productos existentes
        return max(self.productos.keys(), default=0) + 1

    def agregar_producto(self, producto: Producto):
        # Agrega un nuevo producto al inventario si el ID no está en uso
        if producto.id_producto in self.productos:
            print("Error: ID ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado correctamente en memoria.")
            if self.guardar_inventario():
                print("El inventario se ha guardado exitosamente en el archivo.")
            else:
                print("Error al guardar el inventario en el archivo.")

    def eliminar_producto(self, id_producto: int):
        # Elimina un producto del inventario si existe
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente de memoria.")
            if self.guardar_inventario():
                print("El inventario se ha actualizado exitosamente en el archivo.")
            else:
                print("Error al actualizar el inventario en el archivo.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto: int, cantidad: int = None, precio: float = None):
        # Actualiza la cantidad o el precio de un producto si existe
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado correctamente en memoria.")
            if self.guardar_inventario():
                print("El inventario se ha guardado exitosamente en el archivo.")
            else:
                print("Error al guardar el inventario en el archivo.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre: str):
        # Busca productos por nombre (puede haber coincidencias parciales)
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        # Muestra todos los productos en el inventario
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    # Función que maneja el menú interactivo en la consola
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                # Se asigna el ID automáticamente sin solicitarlo al usuario
                nuevo_id = inventario.obtener_siguiente_id()
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(nuevo_id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Ingrese datos válidos para cantidad y precio.")
        elif opcion == "2":
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: Ingrese un ID válido.")
        elif opcion == "3":
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
                precio = input("Nuevo precio (deje en blanco para no cambiar): ")
                inventario.actualizar_producto(
                    id_producto,
                    int(cantidad) if cantidad else None,
                    float(precio) if precio else None
                )
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
