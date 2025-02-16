class Producto:
    # Clase que representa un producto en el inventario
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio = precio  # Precio del producto

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    # Clase que gestiona el inventario de productos
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos con ID como clave
    
    def agregar_producto(self, producto: Producto):
        # Agrega un nuevo producto al inventario si el ID no está en uso
        if producto.id_producto in self.productos:
            print("Error: ID ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado correctamente.")
    
    def eliminar_producto(self, id_producto: int):
        # Elimina un producto del inventario si existe
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")
    
    def actualizar_producto(self, id_producto: int, cantidad: int = None, precio: float = None):
        # Actualiza la cantidad o el precio de un producto si existe
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado correctamente.")
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
        print("\n#### Inicio ####")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Nuevo precio (deje en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)
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
