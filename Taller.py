def registrar_estudiante():
    """
    Permite al usuario registrar un nuevo estudiante.
    Solicita nombre, identificación, edad y al menos 3 notas.
    Implementa validaciones para cada entrada.
    """
    print("\n--- 1. Registrar estudiante ---")
    
    # --- Validación de la identificación ---
    while True:
        try:
            identificacion = input("Ingrese el número de identificación (solo números): ")
            # Se valida que la identificación sea un número y no esté vacía
            if not identificacion.isdigit() or len(identificacion.strip()) == 0:
                print("Error: La identificación debe ser un número válido.")
                continue
            # Se verifica si el estudiante ya existe en el diccionario
            if identificacion in estudiantes:
                print(f"Error: El estudiante con identificación '{identificacion}' ya está registrado.")
                return # Salir de la función si ya existe
            break
        except Exception:
            print("Entrada inválida. Por favor, ingrese un número.")

    # --- Validación del nombre ---
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip().title() # Capitaliza la primera letra de cada palabra
        # Se valida que el nombre no esté vacío y contenga solo letras y espacios
        if len(nombre) > 0 and all(c.isalpha() or c.isspace() for c in nombre):
            break
        else:
            print("Error: El nombre no puede estar vacío y solo debe contener letras.")

    # --- Validación de la edad ---
    while True:
        try:
            edad_str = input("Ingrese la edad del estudiante (1-99): ")
            edad = int(edad_str)
            # Se valida que la edad esté en un rango razonable
            if 1 <= edad <= 99:
                break
            else:
                print("Error: La edad debe ser un número entre 1 y 99.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero para la edad.")

    # --- Validación de las notas ---
    notas = []
    print("Ingrese las notas del estudiante (mínimo 3 notas).")
    while len(notas) < 3:
        try:
            nota_str = input(f"Ingrese la nota #{len(notas) + 1} (0.0 a 5.0): ")
            nota = float(nota_str)
            # Se valida que la nota esté en el rango de 0.0 a 5.0
            if 0.0 <= nota <= 5.0:
                notas.append(nota)
            else:
                print("Error: La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Error: Por favor, ingrese un número decimal válido para la nota.")

    # Se crea el diccionario del estudiante y se añade al diccionario global
    estudiantes[identificacion] = {
        'nombre': nombre,
        'edad': edad,
        'notas': notas
    }
    print(f"\n¡Estudiante '{nombre}' registrado exitosamente con ID: {identificacion}!\n")

def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    # Se valida que la lista de notas no esté vacía para evitar división por cero
    if not notas:
        return 0.0
    # Se usa la función sum() para sumar todos los elementos y len() para contar la cantidad
    return sum(notas) / len(notas)

def consultar_estudiante():
    """
    Permite al usuario consultar la información de un estudiante por su ID.
    Muestra nombre, edad, notas y promedio.
    """
    print("\n--- 2. Consultar estudiante ---")
    identificacion = input("Ingrese el número de identificación del estudiante a consultar: ")
    
    # Se verifica si la identificación existe en el diccionario
    if identificacion in estudiantes:
        estudiante = estudiantes[identificacion]
        promedio = calcular_promedio(estudiante['notas'])
        
        print("\n--- Información del estudiante ---")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Identificación: {identificacion}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Notas: {estudiante['notas']}")
        print(f"Promedio: {promedio:.2f}") # Se formatea el promedio a 2 decimales
        print("-" * 30)
    else:
        # Mensaje de notificación si el estudiante no existe
        print(f"\nError: No se encontró ningún estudiante con la identificación '{identificacion}'.")

def actualizar_notas():
    """
    Permite modificar las notas de un estudiante existente.
    """
    print("\n--- 3. Actualizar notas ---")
    identificacion = input("Ingrese la identificación del estudiante para actualizar sus notas: ")
    
    # Se busca el estudiante en el diccionario
    if identificacion in estudiantes:
        estudiante = estudiantes[identificacion]
        print(f"Estudiante encontrado: {estudiante['nombre']}. Notas actuales: {estudiante['notas']}")
        
        nuevas_notas = []
        print("Ingrese las nuevas notas del estudiante (mínimo 3 notas).")
        while True:
            # Se permite al usuario ingresar nuevas notas hasta que decida detenerse
            # Este ciclo while es diferente al de registro, permite flexibilidad
            try:
                nota_str = input(f"Ingrese la nota #{len(nuevas_notas) + 1} (o 'f' para finalizar): ")
                # El usuario puede escribir 'f' para finalizar la entrada de notas
                if nota_str.lower() == 'f':
                    # Se valida que se hayan ingresado al menos 3 notas
                    if len(nuevas_notas) >= 3:
                        break # Salir del ciclo si hay suficientes notas
                    else:
                        print("Error: Debe ingresar un mínimo de 3 notas.")
                        continue # Continuar pidiendo notas si no se cumple el mínimo
                
                nota = float(nota_str)
                if 0.0 <= nota <= 5.0:
                    nuevas_notas.append(nota)
                else:
                    print("Error: La nota debe estar entre 0.0 y 5.0.")
            except ValueError:
                print("Error: Entrada inválida. Por favor, ingrese un número o 'f'.")
        
        # Se actualizan las notas en el diccionario del estudiante
        estudiante['notas'] = nuevas_notas
        promedio_nuevo = calcular_promedio(nuevas_notas)
        print(f"\n¡Notas de '{estudiante['nombre']}' actualizadas exitosamente!")
        print(f"Nuevo promedio: {promedio_nuevo:.2f}\n")
    else:
        print(f"\nError: No se encontró ningún estudiante con la identificación '{identificacion}'.")

def eliminar_estudiante():
    """
    Permite eliminar el registro de un estudiante por su ID.
    """
    print("\n--- 4. Eliminar estudiante ---")
    identificacion = input("Ingrese el número de identificación del estudiante a eliminar: ")
    
    # Se verifica si la identificación existe
    if identificacion in estudiantes:
        nombre_estudiante = estudiantes[identificacion]['nombre']
        # Se usa del para eliminar el par clave-valor del diccionario
        del estudiantes[identificacion]
        print(f"\n¡El registro de '{nombre_estudiante}' ha sido eliminado exitosamente!\n")
    else:
        print(f"\nError: No se encontró ningún estudiante con la identificación '{identificacion}'.")

def ver_todos_los_estudiantes():
    """
    Muestra una lista de todos los estudiantes registrados con su promedio.
    Usa un ciclo for para recorrer el diccionario.
    """
    print("\n--- 5. Listado general de estudiantes ---")
    
    # Se valida si el diccionario de estudiantes está vacío
    if not estudiantes:
        print("No hay estudiantes registrados en el sistema.")
        return # Salir de la función si no hay estudiantes
    
    # Se usa un bucle for para iterar sobre los elementos del diccionario
    for identificacion, datos_estudiante in estudiantes.items():
        promedio = calcular_promedio(datos_estudiante['notas'])
        print(f"---------------------------------------------------")
        print(f"ID: {identificacion}")
        print(f"Nombre: {datos_estudiante['nombre']}")
        print(f"Edad: {datos_estudiante['edad']}")
        print(f"Promedio general: {promedio:.2f}")
    print("---------------------------------------------------\n")

def mostrar_menu():
    """
    Imprime el menú de opciones para el usuario.
    """
    print("\n" + "="*40)
    print("      SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("="*40)
    print("1. Registrar estudiante")
    print("2. Consultar estudiante")
    print("3. Actualizar notas")
    print("4. Eliminar estudiante")
    print("5. Ver todos los estudiantes")
    print("6. Salir")
    print("="*40)

# ==============================================================================
# FLUJO PRINCIPAL DEL PROGRAMA
# ==============================================================================

# Se utiliza un bucle while para mantener el programa en ejecución
# hasta que el usuario decida salir.
def main():
    """
    Función principal que ejecuta el bucle del programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        # Estructura de control if-elif-else para manejar las opciones del menú
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            consultar_estudiante()
        elif opcion == '3':
            actualizar_notas()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            ver_todos_los_estudiantes()
        elif opcion == '6':
            print("\nGracias por usar el sistema. ¡Hasta luego!\n")
            break # Salir del bucle y finalizar el programa
        else:
            # Mensaje de error para entradas inválidas
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 6.")

# El bloque if __name__ == "__main__": asegura que la función main()
# se ejecute solo cuando el script se corre directamente.
if __name__ == "__main__":
    main()


