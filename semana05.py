#funcion para calcular el area de un triangulo
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

#funcion para calcular el area de un cuadrado
def calcular_area_cuadrado(lado):
    return lado * lado

#funcion principal
def menu():
    #menu usando while
    while True:
        print("-------" * 5)
        print("1. Calcular el área de un triángulo")
        print("2. Calcular el área de un cuadrado")
        print("3. Salir")
        #usantro try para controlar errores de tipo
        try:
            #transformando de texto a entero
            opcion = int(input("Seleccione una opción: "))
            if opcion == 3:
                break
            elif opcion == 1:
                #usando float para calculos mas exactos con decimales
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                area = calcular_area_triangulo(base, altura)
                print(f"El área del triángulo es: {area}")
            elif opcion == 2:
                lado = float(input("Ingrese el lado del cuadrado: "))
                area = calcular_area_cuadrado(lado)
                print(f"El área del cuadrado es: {area}")
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Ejecutar el menú
menu()
