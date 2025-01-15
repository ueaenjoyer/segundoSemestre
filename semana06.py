# Clase base
class Computadora:
    def __init__(self, monitor, cpu, ram, almacenamiento, precio):
        self.monitor = monitor
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.precio = precio
        self.__garantia = 1  # Atributo privado (encapsulación)

    # Método público
    def mostrar_detalles(self):
        return (f"Monitor: {self.monitor}, CPU: {self.cpu}, RAM: {self.ram}GB, "
                f"Almacenamiento: {self.almacenamiento}GB, Precio: ${self.precio}")

    # Método privado (encapsulación)
    def __mostrar_garantia(self):
        return f"Garantía: {self.__garantia} año(s)"

    # Método para acceder a la garantía
    def obtener_garantia(self):
        return self.__mostrar_garantia()


# Clase derivada para una PC Gamer
class CompuGamer(Computadora):
    def __init__(self, monitor, cpu, ram, almacenamiento, precio, grafica):
        super().__init__(monitor, cpu, ram, almacenamiento, precio)
        self.grafica = grafica

    # Sobreescribiendo el método mostrar_detalles (polimorfismo)
    def mostrar_detalles(self):
        detalles_base = super().mostrar_detalles()
        return f"{detalles_base}, Gráfica: {self.grafica}"

# Clase derivada para un Servidor


class Servidor(Computadora):
    def __init__(self, monitor, cpu, ram, almacenamiento, precio, tipo_raid):
        super().__init__(monitor, cpu, ram, almacenamiento, precio)
        self.tipo_raid = tipo_raid

    # Sobreescribiendo el método mostrar_detalles (polimorfismo)
    def mostrar_detalles(self):
        detalles_base = super().mostrar_detalles()
        return f"{detalles_base}, RAID: {self.tipo_raid}"


# Creación de instancias y demostración
compu_gamer = CompuGamer("27 pulgadas", "Intel i9", 32, 1000, 2500, "NVIDIA RTX 3090")
servidor = Servidor("24 pulgadas", "Intel Xeon", 64, 2000, 4000, "RAID 10")

print(compu_gamer.mostrar_detalles())
print(compu_gamer.obtener_garantia())

print(servidor.mostrar_detalles())
print(servidor.obtener_garantia())
