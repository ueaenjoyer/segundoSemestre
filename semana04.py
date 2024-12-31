from datetime import datetime, timedelta

class Tarea:
    def __init__(self, materia, dias_para_entrega, titulo):
        self.__materia = materia  # Encapsulación: atributo privado
        self.__titulo = titulo    # Encapsulación: atributo privado
        self.__fechaentrega = datetime.now() + timedelta(days=dias_para_entrega)
        self.__realizada = False  # Encapsulación: atributo privado

    # Getters y setters para acceder de manera controlada a los atributos privados
    def get_materia(self):
        return self.__materia

    def set_materia(self, materia):
        self.__materia = materia

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_fecha_entrega(self):
        return self.__fechaentrega.strftime("%Y-%m-%d")

    def get_realizada(self):
        return self.__realizada

    def completar_tarea(self):
        """Marca la tarea como realizada."""
        self.__realizada = True
        print(f"La tarea '{self.__titulo}' ha sido marcada como completada.")

    def __str__(self):
        """Devuelve una representación en texto de la tarea."""
        estado = "Realizada" if self.__realizada else "Pendiente"
        return f"Tarea: {self.__titulo} | Materia: {self.__materia} | Fecha de Entrega: {self.get_fecha_entrega()} | Estado: {estado}"


# Clase heredada: TareaPrioritaria (Ejemplo de herencia)
class TareaPrioritaria(Tarea):
    def __init__(self, materia, dias_para_entrega, titulo, prioridad):
        super().__init__(materia, dias_para_entrega, titulo)
        self.__prioridad = prioridad  # Atributo adicional para la clase derivada

    def get_prioridad(self):
        return self.__prioridad

    def set_prioridad(self, prioridad):
        self.__prioridad = prioridad

    def __str__(self):
        """Polimorfismo: Sobreescribimos el método para incluir la prioridad."""
        return super().__str__() + f" | Prioridad: {self.__prioridad}"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self):
        """Agrega una nueva tarea al gestor."""
        titulo = input("Ingrese el título de la tarea: ")
        materia = input("Ingrese el nombre de la materia: ")
        dias_para_entrega = int(input("Ingrese en cuántos días debe entregar la tarea: "))
        es_prioritaria = input("¿Es una tarea prioritaria? (s/n): ").lower() == 's'

        if es_prioritaria:
            prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
            nueva_tarea = TareaPrioritaria(materia, dias_para_entrega, titulo, prioridad)
        else:
            nueva_tarea = Tarea(materia, dias_para_entrega, titulo)

        self.tareas.append(nueva_tarea)
        print(f"Tarea '{titulo}' añadida correctamente.")

    def completar_tarea(self, titulo):
        """Marca una tarea como completada según el título."""
        for tarea in self.tareas:
            if tarea.get_titulo().lower() == titulo.lower():
                tarea.completar_tarea()
                return
        print(f"No se encontró una tarea con el título '{titulo}'.")

    def consultar_tareas_pendientes(self):
        """Muestra todas las tareas pendientes."""
        pendientes = [tarea for tarea in self.tareas if not tarea.get_realizada()]
        if pendientes:
            print("\nTareas pendientes:")
            for tarea in pendientes:
                print(tarea)
        else:
            print("No tienes tareas pendientes.")

    def listar_todas_las_tareas(self):
        """Lista todas las tareas, realizadas y pendientes."""
        if self.tareas:
            print("\nTodas las tareas:")
            for tarea in self.tareas:
                print(tarea)
        else:
            print("No tienes tareas registradas.")


# Uso del sistema de gestión de tareas
gestor = GestorTareas()

while True:
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar Tarea")
    print("2. Completar Tarea")
    print("3. Consultar Tareas Pendientes")
    print("4. Listar Todas las Tareas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        gestor.agregar_tarea()
    elif opcion == "2":
        titulo = input("Ingrese el título de la tarea a completar: ")
        gestor.completar_tarea(titulo)
    elif opcion == "3":
        gestor.consultar_tareas_pendientes()
    elif opcion == "4":
        gestor.listar_todas_las_tareas()
    elif opcion == "5":
        print("Saliendo del gestor de tareas.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
