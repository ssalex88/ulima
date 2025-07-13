import random

# PARÁMETROS CONFIGURABLES

MAX_BUSES = 80        # Máxima cantidad de buses permitidos
MAX_LINEAS = 40       # Máxima cantidad de líneas permitidas
MONTO_MIN = 5000      # Monto mínimo de recaudación
MONTO_MAX = 12000     # Monto máximo de recaudación


# Función que muestra el menú principal

def menu_principal():
    print("\n--- Hola, Ingrese los datos que desea saber ---")
    print("1. Indica la cantidad de buses y líneas que deseas acceder")
    print("2. Mostrar el bus con mayor recaudación")
    print("3. Mostrar el bus con mayor recaudación por línea")
    print("4. Mostrar la línea con menor recaudación de cada bus")
    print("5. Ordenar y mostrar los buses de mayor a menor recaudación (burbuja)")
    print("6. Buscar la recaudación de un bus en una línea (búsqueda lineal)")
    print("7. Intercambiar las recaudaciones de dos buses en una línea")
    print("8. Determinar la suma total recursiva")
    print("9. Salir")

# Solicita cantidad de buses y líneas, validando límites

def capacidad_maxima():
    while True:
        try:
            buses = int(input("Ingrese cantidad de buses que desee que opere: "))
            if 1 < buses <= MAX_BUSES:
                break
            else:
                print(f"Cantidad no aceptada. Debe estar entre 2 y {MAX_BUSES}.")
        except ValueError:
            print("Ingrese un número válido.")

    while True:
        try:
            lineas = int(input("Ingrese cantidad de líneas que desee que funcione con los buses: "))
            if 1 < lineas <= MAX_LINEAS:
                break
            else:
                print(f"Cantidad no aceptada. Debe estar entre 2 y {MAX_LINEAS}.")
        except ValueError:
            print("Ingrese un número válido.")

    return buses, lineas

# Genera matriz aleatoria de recaudaciones por bus y por línea

def generar_recaudaciones(buses, lineas):
    matriz = []
    for _ in range(buses):
        fila = [random.randint(MONTO_MIN, MONTO_MAX) for _ in range(lineas)]
        matriz.append(fila)
    return matriz

# Muestra el bus o los buses con mayor recaudación total

def monto_recaudado(matriz):
    totales = [sum(bus) for bus in matriz]
    max_total = max(totales)
    print("\nEl bus o buses con mayor recaudación de la empresa es:")
    for i, total in enumerate(totales):
        if total == max_total:
            print(f"  Bus {i+1} con S/ {total}")
    return max_total


# Muestra el bus con mayor recaudación en cada línea (por columna)

def max_recaudacion_por_linea(matriz):
    buses = len(matriz)
    lineas = len(matriz[0])
    print("\nBus con mayor recaudación por línea:")
    for linea in range(lineas):
        maximo = matriz[0][linea]
        bus_max = 0
        for bus in range(1, buses):
            if matriz[bus][linea] > maximo:
                maximo = matriz[bus][linea]
                bus_max = bus
        print(f"  Línea {linea+1}: Bus {bus_max+1} con S/ {maximo}")


# Muestra la línea con menor recaudación de cada bus (por fila)

def menor_recuadacion_por_linea(matriz):
    buses = len(matriz)
    lineas = len(matriz[0])
    print("\nLínea con menor recaudación de cada bus:")
    for bus in range(buses):
        menor = matriz[bus][0]
        linea_menor = 0
        for linea in range(1, lineas):
            if matriz[bus][linea] < menor:
                menor = matriz[bus][linea]
                linea_menor = linea
        print(f"  Bus {bus+1}: Línea {linea_menor+1} con S/ {menor}")


# Ordena los buses por recaudación total usando burbuja descendente

def ordenar_buses(matriz):
    n = len(matriz)
    totales = [(i, sum(matriz[i])) for i in range(n)]

    # Algoritmo de burbuja
    for i in range(n - 1):
        for j in range(n - i - 1):
            if totales[j][1] < totales[j + 1][1]:
                totales[j], totales[j + 1] = totales[j + 1], totales[j]

    print("\nBuses ordenados por recaudación (mayor a menor):")
    for bus, total in totales:
        print(f"  Bus {bus+1} con S/ {total}")


# Realiza búsqueda lineal de la recaudación de un bus en una línea

def buscar_recaudacion_lineal(matriz):
    try:
        bus_buscado = int(input("Ingrese el número de bus: "))
        linea_buscada = int(input("Ingrese el número de línea: "))

        encontrado = False
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if (i + 1 == bus_buscado) and (j + 1 == linea_buscada):
                    print(f"Recaudación del bus {bus_buscado} en línea {linea_buscada}: S/ {matriz[i][j]}")
                    encontrado = True
                    break
            if encontrado:
                break

        if not encontrado:
            print("Bus o línea fuera de rango.")
    except:
        print("Entrada inválida.")


# Intercambia las recaudaciones de dos buses en una línea

def intercambiar_recaudaciones(matriz):
    try:
        bus1 = int(input("Ingrese el primer bus: ")) - 1
        bus2 = int(input("Ingrese el segundo bus: ")) - 1
        linea = int(input("Ingrese la línea: ")) - 1
        matriz[bus1][linea], matriz[bus2][linea] = matriz[bus2][linea], matriz[bus1][linea]
        print("Intercambio realizado correctamente.")
    except:
        print("Error en los datos ingresados.")


# Calcula la suma total usando una función recursiva (por filas)

def suma_total_recursiva(matriz):
    def suma_lista(lista):
        if not lista:
            return 0
        return lista[0] + suma_lista(lista[1:])
    total = sum(suma_lista(fila) for fila in matriz)
    print(f"Suma total de todas las recaudaciones: S/ {total}")

# Función principal del programa (ciclo con menú)

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
                buscar_recaudacion_lineal(matriz)
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


# Punto de entrada del programa

if __name__ == "__main__":
    main()
