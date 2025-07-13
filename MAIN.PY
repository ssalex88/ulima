import random

def menu_principal():
    while True:
        print("\n --- Hola, Ingrese los datos que desea saber ---")
        print("1. Indica la cantidad de buses y lineas que deseas acceder: ")
        print("2. Mostrar el bus con mayor recaudacion: ")
        print("3. Mostrar el bus con mayor recaudacion por linea: ")
        print("4. Mostrar la linea con menor recaudacion de cada bus: ")
        print("5. Ordenar y mostrar los buses de mayor a menor recaudacion: ")
        print("6. Encontrar la recaudacion de un bus en una linea determinada: ")
        print("7. Intercambiar las racaudaciones 2 dos buses en una linea: ")
        print("8. Determinar la suma total recursiva: ")
        print("9. Salir ")

# Capacidad maxima de buses y lineas
def capacidad_maxima():
    while True:
        try:
            buses = int(input("Ingrese cantidad de buses que desee que opere: "))
            if buses > 1 and buses <= 80: 
                print("Cantidad de buses accesibles")
                break  # Salir del bucle si la cantidad es válida
            else: 
                print("Cantidad no aceptada. Ingrese una nueva cantidad: ")
        except ValueError:
            print("Ingrese un número válido: ")

    while True:
        try:
            linea = int(input("Ingrese cantidad de líneas que desee que funcione con los buses: "))
            if linea > 1 and linea <= 40:
                print("Cantidad de líneas válida.")
                break  # Salir del bucle si la cantidad es válida
            else:
                print("Cantidad no aceptada. Ingrese una nueva cantidad: ")
        except ValueError:
            print("Ingrese un número válido: ")
    
    return buses, linea

# Recaudaciones aleatorias

def recaudaciones(buses, lineas):
    matriz = []
    for i in range(buses):
        fila = []
        for i in range(lineas):
            fila.append(random.randint(5000, 12000))
        matriz.append(random.randint(fila))
    return matriz

# Bus con mayor recaudacion 

def monto_recaudado(matriz):
    totales = []
    for bus in matriz:
        total = 0
        for n in bus:
            total += n
        totales.append(total)

    valor_max = 0
    if totales:
        valor_max = totales[0]
        for i in range(1, len(totales)):
            if totales[i] > valor_max:
                valor_max = totales[i]

    print("\nEl bus o buses con mayor decaudacion de la empresa es: ")
    i = 0
    bus_max = []
    for total in totales:
        if total == valor_max:
            i += 1
            bus_max.append(i)
            print(f"El bus {i} con {total}")
    return valor_max, bus_max

# Bus con mayor recaudación por línea

def max_recaudacion_por_linea():
    print("Bus con mayor recaudacion por linea")
    for linea in range(lineas):
        maxima_racaudacion = recaudaciones[(0, linea)]
        bus_max = 0
        for bus in range(buses):
            if recaudaciones[(bus, linea)] > maxima_racaudacion:
                maxima_racaudacion = recaudaciones[(bus, linea)]
                bus_max = bus
        print(f"La linea de {linea}: es el {bus_max} con una {maxima_racaudacion}")

# Línea con menor recaudación por bus
def  menor_recuadacion_por_linea():
    print("Bus con menor recaudacion por linea")
    for bus in range(buses):
        menor_recaudacion = recaudaciones[(bus, 0)]
        linea_menor = 0
        for linea in range(lineas):
            if recaudaciones[(bus, linea)] < menor_recaudacion:
                menor_recaudacion = recaudaciones[(bus, linea)]
                linea_menor = linea
        print(f"El bus {bus}: linea {linea_menor} con {menor_recaudacion}")

def ordenar_buses(matriz):
    totales = [(i, sum(matriz[i])) for i in range(len(matriz))]
    totales.sort(key=lambda x: x[1], reverse=True)
    print("\nBuses ordenados por recaudación (mayor a menor):")
    for bus, total in totales:
        print(f"  Bus {bus+1} con S/ {total}")

def buscar_recaudacion(matriz):
    try:
        bus = int(input("Ingrese el número de bus: ")) - 1
        linea = int(input("Ingrese el número de línea: ")) - 1
        print(f"Recaudación del bus {bus+1} en línea {linea+1} es: S/ {matriz[bus][linea]}")
    except:
        print("Valores inválidos o fuera de rango.")

def intercambiar_recaudaciones(matriz):
    try:
        bus1 = int(input("Ingrese el primer bus: ")) - 1
        bus2 = int(input("Ingrese el segundo bus: ")) - 1
        linea = int(input("Ingrese la línea: ")) - 1
        matriz[bus1][linea], matriz[bus2][linea] = matriz[bus2][linea], matriz[bus1][linea]
        print("Intercambio realizado correctamente.")
    except:
        print("Error en los datos ingresados.")

def suma_total_recursiva(matriz):
    def suma_lista(lista):
        if not lista:
            return 0
        return lista[0] + suma_lista(lista[1:])

    total = 0
    for fila in matriz:
        total += suma_lista(fila)
    print(f"Suma total de todas las recaudaciones: S/ {total}")

def main():
    matriz = []
    buses = 0
    lineas = 0

    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buses, lineas = capacidad_maxima()
            matriz = generar_recaudaciones(buses, lineas)
            print("Datos cargados correctamente.")
        elif opcion == "2":
            if matriz:
                monto_recaudado(matriz)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "3":
            if matriz:
                max_recaudacion_por_linea(matriz)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "4":
            if matriz:
                menor_recuadacion_por_linea(matriz)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "5":
            if matriz:
                ordenar_buses(matriz)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "6":
            if matriz:
                buscar_recaudacion(matriz)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "7":
            if matriz:
                intercambiar_recaudaciones(matriz)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "8":
            if matriz:
                suma_total_recursiva(matriz)
            else:
                print("Primero debe ingresar los datos (opción 1).")
        elif opcion == "9":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
