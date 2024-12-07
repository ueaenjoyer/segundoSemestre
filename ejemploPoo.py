from datetime import datetime

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._estado = "Operativo"
        self._fecha_ultimo_mantenimiento = None

    # Método para mostrar la información del vehículo
    def mostrar_informacion(self):
        info = (
            f"Marca: {self._marca}\n"
            f"Modelo: {self._modelo}\n"
            f"Año: {self._año}\n"
            f"Estado: {self._estado}\n"
        )
        if self._fecha_ultimo_mantenimiento:
            info += f"Último mantenimiento: {self._fecha_ultimo_mantenimiento}\n"
        else:
            info += "Último mantenimiento: No registrado\n"
        return info

    # Método para registrar mantenimiento
    def registrar_mantenimiento(self):
        self._estado = "En mantenimiento"
        self._fecha_ultimo_mantenimiento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Mantenimiento registrado.")
        
    # Método para cambiar el estado a operativo
    def cambiar_a_operativo(self):
        self._estado = "Operativo"
        print("El vehículo está ahora operativo.")

 # Implementación de herencia

class VehiculoTransporte(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self._kilometraje = 0  # Inicializa el kilometraje en 0
        self._capacidad_carga = capacidad_carga

    # Método para registrar un viaje, sumando kilómetros al kilometraje
    def registrar_viaje(self, km: float):
        self._kilometraje += km
        print(f"Se han agregado {km} km. Total de kilometraje: {self._kilometraje} km.")

    # Sobrescribir el método mostrar_informacion
    def mostrar_informacion(self):
        info = super().mostrar_informacion()  # Llamada al método de la clase base
        info += f"Kilometraje: {self._kilometraje} km\n"
        info += f"Capacidad de carga: {self._capacidad_carga} toneladas\n"
        return info


class MaquinariaPesada(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)  # Llamada al constructor de la clase base
        self._horometro = 0  # Inicializa el horómetro en 0
        self._tipo = tipo  # Tipo de maquinaria (e.g., retroexcavadora, bulldozer)

    # Método para registrar las horas de trabajo
    def registrar_horas_trabajo(self, horas: float):
        self._horometro += horas
        print(f"Se han agregado {horas} horas. Total de horas de trabajo: {self._horometro} horas.")

    # Método para realizar trabajo específico
    def realizar_trabajo(self):
        print(f"La {self._tipo} está realizando trabajo.")
        
    # Sobrescribir el método mostrar_informacion
    def mostrar_informacion(self):
        info = super().mostrar_informacion()  # Llamada al método de la clase base
        info += f"Horómetro: {self._horometro} horas\n"
        info += f"Tipo de maquinaria: {self._tipo}\n"
        return info


class Gallineta(MaquinariaPesada):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año, "Gallineta")

    # Método para realizar trabajo específico para Gallineta
    def realizar_trabajo(self):
        print("La Gallineta está excavando en terreno.")

class Retroexcavadora(MaquinariaPesada):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año, "Retroexcavadora")

    # Método para realizar trabajo específico para Retroexcavadora
    def realizar_trabajo(self):
        print("La Retroexcavadora está excavando y moviendo tierra.")
