import random
import statistics
import csv

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente:\n")
    mostrar_sueldos_calificados()

def mostrar_sueldos_calificados():
    print("Clasificación de sueldos:")
    menor_800mil = []
    entre_800mil_y_2mill = []
    mayor_2mill = []

    for i, sueldo in enumerate(sueldos):
        nombre = trabajadores[i]
        if sueldo < 800000:
            menor_800mil.append((nombre, sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            entre_800mil_y_2mill.append((nombre, sueldo))
        else:
            mayor_2mill.append((nombre, sueldo))

    print(f"Total de sueldos menores a $800.000:\n{len(menor_800mil)}")
    for nombre, sueldo in menor_800mil:
        print(f"{nombre} Con un sueldo de: ${sueldo}")

    print(f"\nTotal de sueldos entre $800.000 y $2.000.000:\n {len(entre_800mil_y_2mill)}")
    for nombre, sueldo in entre_800mil_y_2mill:
        print(f"{nombre} Con un sueldo de: ${sueldo}")

    print(f"\nTotal de sueldos superiores a $2.000.000:\n {len(mayor_2mill)}")
    for nombre, sueldo in mayor_2mill:
        print(f"{nombre} Con un sueldo de: ${sueldo}")

    total_sueldos = sum(sueldos)
    print(f"\nTotal de todos los sueldos: ${total_sueldos}\n")
    menu()

def ver_estadisticas():
    print("Estadísticas:")
    print(f"Sueldo más alto: ${max(sueldos)}")
    print(f"Sueldo más bajo: ${min(sueldos)}")
    print(f"Promedio de sueldos: ${statistics.mean(sueldos)}")
    print(f"Media geométrica de los sueldos: ${statistics.geometric_mean(sueldos)}\n")
    menu()

def generar_reporte():
    print("Reporte de sueldos:")
    print("Nombre empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido")
    
    with open('sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])

        for i, sueldo in enumerate(sueldos):
            nombre = trabajadores[i]
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([nombre, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"{nombre}, ${sueldo}, ${descuento_salud}, ${descuento_afp}, ${sueldo_liquido}")

    print("\nDatos exportados a sueldos.csv\n")
    menu()

def salir_del_programa():
    print("Finalizando programa...")
    print("Desarrollado por Matias Guzman Arza")
    print("RUT 21.735.700-4")

def menu():
    print("Menú:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    opcion = input("\nIngrese el número de la opción deseada: ")

    if opcion == "1":
        asignar_sueldos_aleatorios()
    elif opcion == "2":
        mostrar_sueldos_calificados()
    elif opcion == "3":
        ver_estadisticas()
    elif opcion == "4":
        generar_reporte()
    elif opcion == "5":
        salir_del_programa()
    else:
        print("Opción inválida. Intente nuevamente.\n")
        menu()

menu()
