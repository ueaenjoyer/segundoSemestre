from datetime import datetime

class Vehiculo:
    def __init__(self, marca, modelo, año, operador, tipo):
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._estado = "Operativo"
        self._fecha_ultimo_mantenimiento = None
        self._operador = operador
        self._tipo = tipo

    # Método para mostrar la información del vehículo
    def mostrar_informacion(self):
        info = (
            f"Marca: {self._marca}\n"
            f"Modelo: {self._modelo}\n"
            f"Año: {self._año}\n"
            f"Estado: {self._estado}\n"
            f"Persona a cargo: {self._operador}\n"
            f"Tipo de vehiculo: {self._tipo}"
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

    def calcular_costo_operativo(self):
        pass  # Este es un método general que no hace nada en la clase base

 # Implementación de herencia

class VehiculoTransporte(Vehiculo):
    def __init__(self, marca, modelo, año, operador, capacidad_carga, tipo):
        super().__init__(marca, modelo, año, operador, tipo)  # Llamada al constructor de la clase base
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

    def calcular_costo_operativo(self):
        costo_por_km = 0.05  # Costo por kilómetro
        costo = self._kilometraje * costo_por_km
        print(f"El costo operativo del vehículo de transporte es: ${costo:.2f}")
        return costo

    

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

    def calcular_costo_operativo(self):
        costo_por_hora = 10  # Costo por hora de uso (ajustable)
        costo = self._horometro * costo_por_hora
        print(f"El costo operativo de la maquinaria pesada es: ${costo:.2f}")
        return costo


# Pruebas
# Crear instancias de vehículos y maquinaria
camioneta = VehiculoTransporte("Toyota", "Hilux", 2020, 1.5)
camion = VehiculoTransporte("Volvo", "FH16", 2019, 25)

gallineta = Gallineta("Caterpillar", "G450", 2021)
retroexcavadora = Retroexcavadora("John Deere", "310L", 2020)

# Mostrar información inicial
print(camioneta.mostrar_informacion())
print(camion.mostrar_informacion())
print(gallineta.mostrar_informacion())
print(retroexcavadora.mostrar_informacion())

# Registrar uso en vehículos de transporte
camioneta.registrar_viaje(120)  # 120 km
camion.registrar_viaje(450)    # 450 km

# Registrar uso en maquinaria pesada
gallineta.registrar_horas_trabajo(5)  # 5 horas
retroexcavadora.registrar_horas_trabajo(8)  # 8 horas

# Mostrar información actualizada
print(camioneta.mostrar_informacion())
print(camion.mostrar_informacion())
print(gallineta.mostrar_informacion())
print(retroexcavadora.mostrar_informacion())

# Registrar mantenimiento
camioneta.registrar_mantenimiento()
retroexcavadora.registrar_mantenimiento()

# Cambiar estado a operativo después del mantenimiento
camioneta.cambiar_a_operativo()
retroexcavadora.cambiar_a_operativo()

# Mostrar información actualizada
print(camioneta.mostrar_informacion())
print(retroexcavadora.mostrar_informacion())

# Listado de todos los vehículos y maquinaria
vehiculos = [camioneta, camion]
maquinarias = [gallineta, retroexcavadora]

# Calcular kilómetros totales recorridos por vehículos de transporte
total_kilometraje = sum(v._kilometraje for v in vehiculos)
print(f"Total de kilómetros recorridos por vehículos de transporte: {total_kilometraje} km")

# Calcular horas totales trabajadas por maquinaria pesada
total_horas = sum(m._horometro for m in maquinarias)
print(f"Total de horas trabajadas por maquinaria pesada: {total_horas} horas")

# Mostrar todos los equipos disponibles
print("Vehículos disponibles:")
for v in vehiculos:
    if v._estado == "Operativo":
        print(v.mostrar_informacion())

print("Maquinaria pesada disponible:")
for m in maquinarias:
    if m._estado == "Operativo":
        print(m.mostrar_informacion())
