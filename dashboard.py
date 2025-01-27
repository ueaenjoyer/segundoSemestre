import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Definir la ruta base donde se encuentra el script
    ruta_base = os.path.dirname(__file__)

    print("\n===============================================")
    print("       Bienvenido al Dashboard de Scripts      ")
    print("           ( ͡° ͜ʖ ͡°) ¡Vamos a divertirnos!      ")
    print("===============================================")

    while True:
        print("\nMenu Principal - ¡Elige un script para ver y ejecutar!")
        scripts = [f.name for f in os.scandir(ruta_base) if f.is_file() and f.name.endswith('.py')]

        # Si no hay scripts en el directorio, muestra un mensaje
        if not scripts:
            print("No se encontraron scripts en este directorio.")
            break

        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Salir")

        eleccion_script = input("Elige un script o '0' para salir: ")
        if eleccion_script == '0':
            print("Saliendo del programa... Adiós! ✌️")
            break
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_base, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Deseas ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script. 😅")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
