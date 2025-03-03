import json
import os
from datetime import datetime

class Producto:
    """Clase para representar un producto en el inventario"""
    
    def __init__(self, id, nombre, cantidad, precio):
        """Constructor de la clase Producto
        
        Args:
            id (str): Identificador único del producto
            nombre (str): Nombre del producto
            cantidad (int): Cantidad disponible en inventario
            precio (float): Precio unitario del producto
        """
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor que cero")
    
    def to_dict(self):
        """Convierte el objeto Producto a un diccionario para serialización JSON"""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }
    
    @classmethod
    def from_dict(cls, dict_data):
        """Crea un objeto Producto a partir de un diccionario
        
        Args:
            dict_data (dict): Diccionario con los datos del producto
            
        Returns:
            Producto: Nueva instancia de Producto
        """
        return cls(
            dict_data['id'],
            dict_data['nombre'],
            dict_data['cantidad'],
            dict_data['precio']
        )
    
    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"


class Inventario:
    """Clase para gestionar la colección de productos"""
    
    def __init__(self):
        """Constructor de la clase Inventario"""
        # Diccionario para almacenar productos, usando ID como clave para búsqueda rápida
        self._productos = {}
        # Conjunto para mantener IDs usados y garantizar unicidad
        self._ids_usados = set()
        # Diccionario para indexar productos por nombre para búsquedas eficientes
        self._indice_nombre = {}
    
    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario
        
        Args:
            producto (Producto): Producto a agregar
            
        Returns:
            bool: True si se agregó exitosamente, False si el ID ya existe
        """
        if producto.id in self._ids_usados:
            return False
        
        # Agregar producto al diccionario principal
        self._productos[producto.id] = producto
        self._ids_usados.add(producto.id)
        
        # Actualizar índice por nombre
        nombre_lower = producto.nombre.lower()
        if nombre_lower not in self._indice_nombre:
            self._indice_nombre[nombre_lower] = []
        self._indice_nombre[nombre_lower].append(producto.id)
        
        return True
    
    def eliminar_producto(self, id):
        """Elimina un producto del inventario
        
        Args:
            id (str): ID del producto a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False si no se encontró
        """
        if id not in self._productos:
            return False
        
        # Eliminar de los índices
        producto = self._productos[id]
        nombre_lower = producto.nombre.lower()
        
        if nombre_lower in self._indice_nombre:
            if id in self._indice_nombre[nombre_lower]:
                self._indice_nombre[nombre_lower].remove(id)
                if not self._indice_nombre[nombre_lower]:
                    del self._indice_nombre[nombre_lower]
        
        # Eliminar del diccionario principal y del conjunto de IDs
        del self._productos[id]
        self._ids_usados.remove(id)
        
        return True
    
    def actualizar_cantidad(self, id, nueva_cantidad):
        """Actualiza la cantidad de un producto
        
        Args:
            id (str): ID del producto a actualizar
            nueva_cantidad (int): Nueva cantidad del producto
            
        Returns:
            bool: True si se actualizó correctamente, False si no se encontró
        """
        if id not in self._productos:
            return False
        
        try:
            self._productos[id].cantidad = nueva_cantidad
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def actualizar_precio(self, id, nuevo_precio):
        """Actualiza el precio de un producto
        
        Args:
            id (str): ID del producto a actualizar
            nuevo_precio (float): Nuevo precio del producto
            
        Returns:
            bool: True si se actualizó correctamente, False si no se encontró
        """
        if id not in self._productos:
            return False
        
        try:
            self._productos[id].precio = nuevo_precio
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre
        
        Args:
            nombre (str): Nombre o parte del nombre a buscar
            
        Returns:
            list: Lista de productos que coinciden con la búsqueda
        """
        resultados = []
        nombre_lower = nombre.lower()
        
        # Búsqueda por coincidencia exacta usando el índice
        if nombre_lower in self._indice_nombre:
            for id in self._indice_nombre[nombre_lower]:
                resultados.append(self._productos[id])
        
        # Búsqueda por coincidencia parcial
        for nombre_indice in self._indice_nombre:
            if nombre_lower in nombre_indice and nombre_lower != nombre_indice:
                for id in self._indice_nombre[nombre_indice]:
                    resultados.append(self._productos[id])
        
        return resultados
    
    def obtener_producto(self, id):
        """Obtiene un producto por su ID
        
        Args:
            id (str): ID del producto
            
        Returns:
            Producto: Producto encontrado o None si no existe
        """
        return self._productos.get(id)
    
    def listar_productos(self):
        """Obtiene todos los productos del inventario
        
        Returns:
            list: Lista de todos los productos
        """
        return list(self._productos.values())
    
    def generar_id(self):
        """Genera un nuevo ID único para un producto
        
        Returns:
            str: ID único generado
        """
        # Generar ID basado en timestamp + número aleatorio
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Encontrar el siguiente número disponible
        contador = 1
        nuevo_id = f"P{timestamp}{contador:03d}"
        
        while nuevo_id in self._ids_usados:
            contador += 1
            nuevo_id = f"P{timestamp}{contador:03d}"
        
        return nuevo_id
    
    def guardar_en_archivo(self, ruta_archivo="inventario.json"):
        """Guarda el inventario en un archivo JSON
        
        Args:
            ruta_archivo (str): Ruta del archivo donde guardar
            
        Returns:
            bool: True si se guardó correctamente, False si hubo error
        """
        try:
            # Convertir cada producto a diccionario
            datos = {id: producto.to_dict() for id, producto in self._productos.items()}
            
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")
            return False
    
    def cargar_desde_archivo(self, ruta_archivo="inventario.json"):
        """Carga el inventario desde un archivo JSON
        
        Args:
            ruta_archivo (str): Ruta del archivo desde donde cargar
            
        Returns:
            bool: True si se cargó correctamente, False si hubo error
        """
        try:
            if not os.path.exists(ruta_archivo):
                print(f"El archivo {ruta_archivo} no existe. Se creará un inventario vacío.")
                return True
            
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            
            # Limpiar inventario actual
            self._productos.clear()
            self._ids_usados.clear()
            self._indice_nombre.clear()
            
            # Cargar productos desde el archivo
            for id, datos_producto in datos.items():
                producto = Producto.from_dict(datos_producto)
                self.agregar_producto(producto)
            
            return True
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
            return False


class SistemaInventario:
    """Clase principal para gestionar el sistema de inventario"""
    
    def __init__(self, ruta_archivo="inventario.json"):
        """Constructor de la clase SistemaInventario
        
        Args:
            ruta_archivo (str): Ruta del archivo de inventario
        """
        self.inventario = Inventario()
        self.ruta_archivo = ruta_archivo
        self.inventario.cargar_desde_archivo(ruta_archivo)
    
    def mostrar_menu(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "="*50)
        print("    SISTEMA DE GESTIÓN DE INVENTARIO")
        print("="*50)
        print("1. Agregar nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad de un producto")
        print("4. Actualizar precio de un producto")
        print("5. Buscar productos por nombre")
        print("6. Mostrar todos los productos")
        print("7. Guardar inventario")
        print("8. Salir")
        print("="*50)
    
    def ejecutar(self):
        """Ejecuta el sistema de inventario"""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción (1-8): ")
            
            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.eliminar_producto()
            elif opcion == "3":
                self.actualizar_cantidad()
            elif opcion == "4":
                self.actualizar_precio()
            elif opcion == "5":
                self.buscar_por_nombre()
            elif opcion == "6":
                self.mostrar_todos()
            elif opcion == "7":
                self.guardar_inventario()
            elif opcion == "8":
                self.guardar_inventario()
                print("\nGuardando inventario antes de salir...")
                print("¡Gracias por usar el Sistema de Gestión de Inventario!")
                break
            else:
                print("\nOpción no válida. Por favor, intente de nuevo.")
    
    def agregar_producto(self):
        """Agrega un nuevo producto al inventario"""
        print("\n----- AGREGAR NUEVO PRODUCTO -----")
        
        # Generar ID automáticamente
        id = self.inventario.generar_id()
        print(f"ID asignado: {id}")
        
        nombre = input("Nombre del producto: ")
        
        # Validar cantidad
        while True:
            try:
                cantidad = int(input("Cantidad en inventario: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        # Validar precio
        while True:
            try:
                precio = float(input("Precio unitario: $"))
                if precio <= 0:
                    print("El precio debe ser mayor que cero. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        # Crear y agregar el producto
        producto = Producto(id, nombre, cantidad, precio)
        if self.inventario.agregar_producto(producto):
            print(f"\nProducto '{nombre}' agregado exitosamente con ID: {id}")
        else:
            print("\nError: No se pudo agregar el producto. El ID ya existe.")
    
    def eliminar_producto(self):
        """Elimina un producto del inventario"""
        print("\n----- ELIMINAR PRODUCTO -----")
        id = input("Ingrese el ID del producto a eliminar: ")
        
        producto = self.inventario.obtener_producto(id)
        if producto:
            print(f"\nProducto encontrado: {producto}")
            confirmacion = input("¿Está seguro de eliminar este producto? (s/n): ").lower()
            
            if confirmacion == 's':
                if self.inventario.eliminar_producto(id):
                    print(f"\nProducto con ID '{id}' eliminado exitosamente.")
                else:
                    print(f"\nError: No se pudo eliminar el producto con ID '{id}'.")
            else:
                print("\nOperación cancelada.")
        else:
            print(f"\nNo se encontró ningún producto con ID '{id}'.")
    
    def actualizar_cantidad(self):
        """Actualiza la cantidad de un producto"""
        print("\n----- ACTUALIZAR CANTIDAD -----")
        id = input("Ingrese el ID del producto: ")
        
        producto = self.inventario.obtener_producto(id)
        if producto:
            print(f"\nProducto encontrado: {producto}")
            
            # Validar nueva cantidad
            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa. Intente de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero válido.")
            
            if self.inventario.actualizar_cantidad(id, nueva_cantidad):
                print(f"\nCantidad del producto con ID '{id}' actualizada a {nueva_cantidad}.")
            else:
                print(f"\nError: No se pudo actualizar la cantidad del producto.")
        else:
            print(f"\nNo se encontró ningún producto con ID '{id}'.")
    
    def actualizar_precio(self):
        """Actualiza el precio de un producto"""
        print("\n----- ACTUALIZAR PRECIO -----")
        id = input("Ingrese el ID del producto: ")
        
        producto = self.inventario.obtener_producto(id)
        if producto:
            print(f"\nProducto encontrado: {producto}")
            
            # Validar nuevo precio
            while True:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: $"))
                    if nuevo_precio <= 0:
                        print("El precio debe ser mayor que cero. Intente de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            if self.inventario.actualizar_precio(id, nuevo_precio):
                print(f"\nPrecio del producto con ID '{id}' actualizado a ${nuevo_precio:.2f}.")
            else:
                print(f"\nError: No se pudo actualizar el precio del producto.")
        else:
            print(f"\nNo se encontró ningún producto con ID '{id}'.")
    
    def buscar_por_nombre(self):
        """Busca productos por nombre"""
        print("\n----- BUSCAR PRODUCTOS POR NOMBRE -----")
        nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
        
        resultados = self.inventario.buscar_por_nombre(nombre)
        
        if resultados:
            print(f"\nSe encontraron {len(resultados)} productos:")
            for i, producto in enumerate(resultados, 1):
                print(f"{i}. {producto}")
        else:
            print(f"\nNo se encontraron productos que coincidan con '{nombre}'.")
    
    def mostrar_todos(self):
        """Muestra todos los productos en el inventario"""
        print("\n----- TODOS LOS PRODUCTOS EN INVENTARIO -----")
        productos = self.inventario.listar_productos()
        
        if productos:
            print(f"\nTotal de productos: {len(productos)}")
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto}")
        else:
            print("\nEl inventario está vacío.")
    
    def guardar_inventario(self):
        """Guarda el inventario en el archivo"""
        print("\nGuardando inventario...")
        if self.inventario.guardar_en_archivo(self.ruta_archivo):
            print(f"Inventario guardado exitosamente en '{self.ruta_archivo}'.")
        else:
            print("Error: No se pudo guardar el inventario.")


if __name__ == "__main__":
    # Iniciar el sistema
    sistema = SistemaInventario()
    sistema.ejecutar()