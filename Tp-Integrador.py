import csv

# ---------- FUNCIONES ---------- #

def leer_csv(archivo_csv="Paises.csv"):
    """Lee el CSV y devuelve encabezado y datos (sin duplicados)"""
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = list(csv.reader(archivo))
        encabezado = lector[0]
        datos = lector[1:]

        paises_unicos = {}
        for fila in datos:
            if fila[0] not in paises_unicos:
                paises_unicos[fila[0]] = fila
        return encabezado, list(paises_unicos.values())

def buscar_pais(nombre, archivo_csv="Paises.csv"):
    """Busca un país por nombre en el CSV"""
    _, datos = leer_csv(archivo_csv)
    for fila in datos:
        if nombre.strip().lower() == fila[0].strip().lower():
            return fila
    return None

def filtrar_por_continente(archivo_csv="Paises.csv"):
    """Filtra países por continente"""
    _, datos = leer_csv(archivo_csv)
    continente = input("Ingrese el continente: ").strip().lower()
    encontrados = [fila for fila in datos if continente == fila[3].strip().lower()]

    if encontrados:
        print(f"\nPaíses encontrados en {continente.capitalize()}:")
        for f in encontrados:
            print(f)
    else:
        print("⚠️ No se encontraron países para ese continente.")

def filtrar_por_rango(archivo_csv="Paises.csv", tipo="poblacion"):
    """Filtra países por rango de población o superficie"""
    try:
        minimo = int(input(f"Ingrese valor mínimo de {tipo}: "))
        maximo = int(input(f"Ingrese valor máximo de {tipo}: "))
    except ValueError:
        print("⚠️ Debe ingresar números válidos")
        return
    
    _, datos = leer_csv(archivo_csv)
    col = 1 if tipo == "poblacion" else 2
    encontrados = [fila for fila in datos if minimo <= int(fila[col]) <= maximo]

    if encontrados:
        print(f"\nPaíses encontrados en el rango de {tipo}:")
        for f in encontrados:
            print(f)
    else:
        print(f"⚠️ No se encontraron países en el rango de {tipo}.")

def ordenar_paises_nombre(archivo_csv="Paises.csv"):
    _, datos = leer_csv(archivo_csv)
    datos.sort(key=lambda x: x[0].lower())
    print("\nPaíses ordenados por Nombre:")
    for fila in datos:
        print(fila[0])

def ordenar_paises_poblacion(archivo_csv="Paises.csv"):
    _, datos = leer_csv(archivo_csv)
    for fila in datos:
        fila[1] = int(fila[1])
    datos.sort(key=lambda x: x[1])
    print("\nPaíses ordenados por Población:")
    for fila in datos:
        print(f"{fila[0]}: {fila[1]}")

def ordenar_paises_superficie(archivo_csv="Paises.csv", reverse=False):
    _, datos = leer_csv(archivo_csv)
    for fila in datos:
        fila[2] = int(fila[2])
    datos.sort(key=lambda x: x[2], reverse=reverse)
    print("\nPaíses ordenados por Superficie:")
    for fila in datos:
        print(f"{fila[0]}: {fila[2]}")

def mostrar_estadisticas_poblacion(archivo_csv="Paises.csv"):
    _, datos = leer_csv(archivo_csv)
    poblacion_mayor = 0
    pais_mayor = ""
    for fila in datos:
        fila[1] = int(fila[1])
        if fila[1] > poblacion_mayor:
            poblacion_mayor = fila[1]
            pais_mayor = fila[0]
    print(f"La mayor población es: {poblacion_mayor} ({pais_mayor})")

def mostrar_estadisticas_poblacion_menor(archivo_csv="Paises.csv"):
    _, datos = leer_csv(archivo_csv)
    if not datos:
        print("No hay datos disponibles.")
        return
    datos[0][1] = int(datos[0][1])
    poblacion_menor = datos[0][1]
    pais_menor = datos[0][0]
    for fila in datos:
        fila[1] = int(fila[1])
        if fila[1] < poblacion_menor:
            poblacion_menor = fila[1]
            pais_menor = fila[0]
    print(f"La menor población es: {poblacion_menor} ({pais_menor})")

def mostrar_estadisticas_promedio(archivo_csv="Paises.csv"):
    _, datos = leer_csv(archivo_csv)
    if not datos:
        print("No hay datos disponibles.")
        return
    poblaciones = 0
    contador = 0
    for fila in datos:
        poblaciones += int(fila[1])
        contador += 1
    promedio = poblaciones / contador
    print("\n📊 Población Promedio:", promedio)

def mostrar_estadisticas_completas(archivo_csv="Paises.csv"):
    _, datos = leer_csv(archivo_csv)
    if not datos:
        print("No hay datos disponibles.")
        return

    poblaciones = [int(fila[1]) for fila in datos]
    superficies = [int(fila[2]) for fila in datos]

    total_paises = len(datos)
    total_poblacion = sum(poblaciones)
    promedio_poblacion = total_poblacion / total_paises
    max_poblacion = max(poblaciones)
    min_poblacion = min(poblaciones)

    pais_mas_poblado = [f[0] for f in datos if int(f[1]) == max_poblacion][0]
    pais_menos_poblado = [f[0] for f in datos if int(f[1]) == min_poblacion][0]

    print("\n📊 Estadísticas Generales:")
    print(f"Total de países: {total_paises}")
    print(f"Población total: {total_poblacion}")
    print(f"Población promedio: {promedio_poblacion:.2f}")
    print(f"País más poblado: {pais_mas_poblado} ({max_poblacion})")
    print(f"País menos poblado: {pais_menos_poblado} ({min_poblacion})")


# ---------- MENÚ PRINCIPAL ---------- #

def menu_principal():
    opcion = 0
    while opcion != 5:
        print("""\n=== Menú Principal ===
1 - Buscar País
2 - Filtrado de Países
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
                print("✅ País encontrado:", resultado)
            else:
                print("❌ País no encontrado")

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

        elif opcion == 3:
            sub = 0
            while sub != 4:
                print("""\n--- Menú Ordenado ---
1 - Ordenar por Nombre
2 - Ordenar por Población
3 - Ordenar por Superficie
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
                elif sub == 3:
                    sub_sub_menu = 0
                    while sub_sub_menu != 3:
                        print("""\n--- Menú Ordenar por Superficie ---
1 - Ordenar de menor a mayor
2 - Ordenar de mayor a menor
3 - Volver al Menú Anterior""")
                        try:
                            sub_sub_menu = int(input("Ingrese una opción: "))
                        except ValueError:
                            print("⚠️ Entrada inválida. Debe ingresar un número.")
                            continue
                        if sub_sub_menu == 1:
                            ordenar_paises_superficie()
                        elif sub_sub_menu == 2:
                            ordenar_paises_superficie(reverse=True)
                elif sub == 4:
                    print("🔙 Volviendo al menú principal...")

        elif opcion == 4:
            sub_sub_menu = 0
            while sub_sub_menu != 5:
                print("""\n--- Menú Estadísticas ---
1 - País con mayor población
2 - País con menor población
3 - Población Promedio
4 - Estadísticas Completas
5 - Volver al Menú Principal""")
                try:
                    sub_sub_menu = int(input("Ingrese una opción: "))
                except ValueError:
                    print("⚠️ Entrada inválida. Debe ingresar un número.")
                    continue
                if sub_sub_menu == 1:
                    mostrar_estadisticas_poblacion()
                elif sub_sub_menu == 2:
                    mostrar_estadisticas_poblacion_menor()
                elif sub_sub_menu == 3:
                    mostrar_estadisticas_promedio()
                elif sub_sub_menu == 4:
                    mostrar_estadisticas_completas()
                elif sub_sub_menu == 5:
                    print("🔙 Volviendo al menú principal...")

        elif opcion == 5:
            print("Gracias por usar el programa, hasta luego! 👋")

# Ejecutar menú
menu_principal()
