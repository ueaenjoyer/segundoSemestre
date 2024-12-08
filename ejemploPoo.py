from datetime import datetime

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo, anio, operador, tipo):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._estado = "Operativo"
        self._fecha_ultimo_mantenimiento = None
        self._operador = operador
        self._tipo = tipo

    def mostrar_informacion(self):
        info = (
            f"Marca: {self._marca}\n"
            f"Modelo: {self._modelo}\n"
            f"Año: {self._anio}\n"
            f"Estado: {self._estado}\n"
            f"Operador: {self._operador}\n"
            f"Tipo: {self._tipo}\n"
        )
        if self._fecha_ultimo_mantenimiento:
            info += f"Último mantenimiento: {self._fecha_ultimo_mantenimiento}\n"
        else:
            info += "Último mantenimiento: No registrado\n"
        return info

    def registrar_mantenimiento(self):
        self._estado = "En mantenimiento"
        self._fecha_ultimo_mantenimiento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Mantenimiento registrado.")

    def cambiar_a_operativo(self):
        self._estado = "Operativo"
        print("El vehículo está ahora operativo.")

# Subclase Vehículo de Transporte
class VehiculoTransporte(Vehiculo):
    def __init__(self, marca, modelo, anio, operador, capacidad_carga):
        super().__init__(marca, modelo, anio, operador, "Vehículo de Transporte")
        self._kilometraje = 0
        self._capacidad_carga = capacidad_carga

    def registrar_viaje(self, km):
        self._kilometraje += km
        print(f"{km} km añadidos. Total: {self._kilometraje} km.")

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f"Kilometraje: {self._kilometraje} km\n"
        info += f"Capacidad de carga: {self._capacidad_carga} toneladas\n"
        return info

# Subclase Maquinaria Pesada
class MaquinariaPesada(Vehiculo):
    def __init__(self, marca, modelo, anio, operador, tipo_maquinaria):
        super().__init__(marca, modelo, anio, operador, "Maquinaria Pesada")
        self._horometro = 0
        self._tipo_maquinaria = tipo_maquinaria

    def registrar_horas_trabajo(self, horas):
        self._horometro += horas
        print(f"{horas} horas añadidas. Total: {self._horometro} horas.")

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f"Horómetro: {self._horometro} horas\n"
        info += f"Tipo de maquinaria: {self._tipo_maquinaria}\n"
        return info

# Lista global de vehículos
vehiculos = []

# Menú CRUD
while True:
    print("\n------- Control y registro de vehículos -------")
    print("1. Ingresar vehículo")
    print("2. Ver vehículos")
    print("3. Editar vehículo")
    print("4. Eliminar vehículo")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("1. Vehículo de transporte")
        print("2. Maquinaria pesada")
        tipo = input("Seleccione el tipo de vehículo: ")

        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        anio = int(input("Ingrese el año: "))
        operador = input("Ingrese el operador: ")

        if tipo == "1":
            capacidad_carga = float(input("Ingrese la capacidad de carga (en toneladas): "))
            vehiculo = VehiculoTransporte(marca, modelo, anio, operador, capacidad_carga)
        elif tipo == "2":
            tipo_maquinaria = input("Ingrese el tipo de maquinaria (e.g., Gallineta, Retroexcavadora): ")
            vehiculo = MaquinariaPesada(marca, modelo, anio, operador, tipo_maquinaria)
        else:
            print("Opción inválida.")
            continue

        vehiculos.append(vehiculo)
        print("Vehículo registrado exitosamente.")

    elif opcion == "2":
        if not vehiculos:
            print("No hay vehículos registrados.")
        else:
            for i, vehiculo in enumerate(vehiculos, 1):
                print(f"\n--- Vehículo {i} ---")
                print(vehiculo.mostrar_informacion())

    elif opcion == "3":
        if not vehiculos:
            print("No hay vehículos registrados.")
        else:
            for i, vehiculo in enumerate(vehiculos, 1):
                print(f"{i}. {vehiculo._marca} {vehiculo._modelo}")
            indice = int(input("Seleccione el número del vehículo a editar: ")) - 1

            if 0 <= indice < len(vehiculos):
                vehiculo = vehiculos[indice]
                vehiculo._operador = input("Ingrese el nuevo operador: ")
                print("Operador actualizado.")
            else:
                print("Selección inválida.")

    elif opcion == "4":
        if not vehiculos:
            print("No hay vehículos registrados.")
        else:
            for i, vehiculo in enumerate(vehiculos, 1):
                print(f"{i}. {vehiculo._marca} {vehiculo._modelo}")
            indice = int(input("Seleccione el número del vehículo a eliminar: ")) - 1

            if 0 <= indice < len(vehiculos):
                eliminado = vehiculos.pop(indice)
                print(f"Vehículo {eliminado._marca} {eliminado._modelo} eliminado.")
            else:
                print("Selección inválida.")

    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
