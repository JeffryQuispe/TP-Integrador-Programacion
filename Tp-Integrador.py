import csv
# ---------- FUNCIONES ---------- #

def buscar_pais(nombre, archivo_csv="Paises.csv"):
    """Busca un país por nombre en el CSV"""
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if nombre.strip().lower() == fila[0].strip().lower():
                return fila
    return None

def filtrar_por_continente(archivo_csv="Paises.csv"):
    """Filtra países por continente"""
    continente = input("Ingrese el continente: ").strip().lower()
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        encontrados = []
        for fila in lector:
            if continente == fila[3].strip().lower():
                encontrados.append(fila)
    if encontrados:
        print(f"Países encontrados en {continente.capitalize()}:")
        for f in encontrados:
            print(f)
    else:
        print("No se encontraron países para ese continente.")

def filtrar_por_rango(archivo_csv="Paises.csv", tipo="poblacion"):
    """Filtra países por rango de población o superficie"""
    try:
        minimo = int(input(f"Ingrese valor mínimo de {tipo}: "))
        maximo = int(input(f"Ingrese valor máximo de {tipo}: "))
    except ValueError:
        print("⚠️ Debe ingresar números válidos")
        return
    
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        encontrados = []
        for fila in lector:
            valor = int(fila[1] if tipo=="poblacion" else fila[2])
            if minimo <= valor <= maximo:
                encontrados.append(fila)
    if encontrados:
        print(f"Países encontrados en el rango de {tipo}:")
        for f in encontrados:
            print(f)
    else:
        print(f"No se encontraron países en el rango de {tipo}.")

def ordenar_paises_nombre(archivo_csv="Paises.csv"):
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = list(csv.reader(archivo))
        lector.sort(key=lambda x: str(x[0]))
        print("Países ordenados por Nombre:")
        for fila in lector:
            print(fila[0])

def ordenar_paises_poblacion(archivo_csv="paises.csv"):
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = list(csv.reader(archivo))
        encabezado = lector[0]
        datos = lector[1:]
        for P in datos:
            P[1] = int(P[1])
        datos.sort(key=lambda x: x[1])
        print("Países ordenados por Población:")
        for fila in datos:
            print(f"{fila[0]}: {fila[1]}")

def mostrar_estadisticas(archivo_csv="Paises.csv"):
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        total_paises = 0
        total_poblacion = 0
        for fila in lector:
            total_paises += 1
            total_poblacion += int(fila[1])
        print(f"Total de países: {total_paises}")
        print(f"Población total: {total_poblacion}")


# ---------- MENÚ PRINCIPAL ---------- #

def menu_principal():
    opcion = 0
    while opcion != 5:
        print("""\n=== Menú Principal ===
1 - Buscar País
2 - Filtrado Países
3 - Ordenado de Países
4 - Estadísticas
5 - Salir""")
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("⚠️ Entrada inválida. Debe ingresar un número.")
            continue

        if opcion == 1:
            nombre = input("Ingrese el nombre del país que desea buscar: ")
            resultado = buscar_pais(nombre)
            if resultado:
                print("País encontrado:", resultado)
            else:
                print("País no encontrado")

        elif opcion == 2:
            sub = 0
            while sub != 4:
                print("""\n--- Menú Filtrado ---
1 - Continente
2 - Rango de Población
3 - Rango de Superficie
4 - Volver al Menú Principal""")
                try:
                    sub = int(input("Ingrese una opción: "))
                except ValueError:
                    print("⚠️ Entrada inválida. Debe ingresar un número.")
                    continue

                if sub == 1:
                    filtrar_por_continente()
                elif sub == 2:
                    filtrar_por_rango(tipo="poblacion")
                elif sub == 3:
                    filtrar_por_rango(tipo="superficie")
                elif sub == 4:
                    print("🔙 Volviendo al menú principal...")
                else:
                    print("⚠️ Opción no válida, intente de nuevo.")

        elif opcion == 3:
            sub = 0
            while sub != 2:
                print("""\n--- Menú Ordenado ---
1 - Ordenar por Nombre
2 - Ordenar por Población
3 - Ordenar nar por Superficie
4 - Volver al Menú Principal""")                     
                try:
                    sub = int(input("Ingrese una opción: "))
                except ValueError:
                    print("⚠️ Entrada inválida. Debe ingresar un número.")
                    continue
                if sub == 1:
                    ordenar_paises_nombre()
                elif sub == 2:
                    ordenar_paises_poblacion()

        elif opcion == 4:
            mostrar_estadisticas()

        elif opcion == 5:
            print("Gracias por usar el programa, hasta luego! 👋")
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

# Ejecutar menú
menu_principal()
