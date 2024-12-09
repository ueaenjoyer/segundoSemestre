# Prograamcion tradicional
# Determinar el promedio semanal del clima.

tem_por_dias = [] #lista para guardar la temperatura de los dias de la semana

def ingresar_tem_diaria():#funcion para ingresar los valores de temperatura a la lista
    dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sábado", "domingo"]
    temperaturas = []
    for i in dias_semana:
        temperaturas.append(float(input(f"Ingrese temperatura del dia {i}: ")))
    return temperaturas

tem_por_dias = ingresar_tem_diaria()


def calcular_promedio_semanal(tem_dias):
    suma = 0
    for i in tem_dias:
        suma += i
    promedio = suma/len(tem_dias)
    return promedio

print(calcular_promedio_semanal(tem_por_dias))


# Programación Orientada a Objetos
# Determinar el promedio semanal del clima.

class ClimaSemanal:
    def __init__(self):
        # Inicializa la lista de temperaturas
        self.temperaturas = []

    def ingresar_temperaturas(self):
        # Solicita las temperaturas para los días de la semana
        dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sábado", "domingo"]
        for dia in dias_semana:
            while True:
                try:
                    temp = float(input(f"Ingrese temperatura del día {dia}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        # Calcula el promedio de las temperaturas
        if len(self.temperaturas) == 0:
            return 0  # Si no hay temperaturas, retorna 0
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio


# Crear una instancia de ClimaSemanal
clima = ClimaSemanal()

# Ingresar las temperaturas
clima.ingresar_temperaturas()

# Calcular y mostrar el promedio
promedio = clima.calcular_promedio()
print(f"El promedio semanal del clima es: {promedio:.2f}")
