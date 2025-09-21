import csv

# ---------- FUNCIONES ----------- #

#------ Buscar ------------------#
def buscar_pais(prefijo):
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)  # salta encabezado
        encontrados = []
        for fila in leer:
            if fila[0].lower().startswith(prefijo.lower().strip()):
                encontrados.append(fila)
        return encontrados

#-------- Filtrado Paises  -------#
def continentes(continente):
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)
        resultado = []
        for fila in leer:
            if fila[3].lower().strip() == continente.lower().strip():
                resultado.append(fila)
        return resultado

# ------ Rango Población ------- #
def rango_poblacion(min_pob, max_pob):
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)
        for fila in leer:
            poblacion = int(fila[1])
            if min_pob <= poblacion <= max_pob:
                print(f"País: {fila[0]} - Población: {poblacion}")

#------- Rango Superficie -------#
def rango_superficie(min_sup, max_sup, descendente=False):
    resultados = []
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)
        for fila in leer:
            superficie = int(fila[2])
            if min_sup <= superficie <= max_sup:
                resultados.append((fila[0], superficie))
    resultados.sort(key=lambda x: x[1], reverse=descendente)
    for pais, sup in resultados:
        print(f"País: {pais} - Superficie: {sup}")

#------ Mayor y Menor Población -----#
def mayor_menor_poblacion():
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)
        max_pais = ("", 0)
        min_pais = ("", float('inf'))
        for fila in leer:
            poblacion = int(fila[1])
            if poblacion > max_pais[1]:
                max_pais = (fila[0], poblacion)
            if poblacion < min_pais[1]:
                min_pais = (fila[0], poblacion)
        print(f"🟢 Mayor población: {max_pais[0]} con {max_pais[1]}")
        print(f"🔴 Menor población: {min_pais[0]} con {min_pais[1]}")

#------- Promedio Población------#
def promedio_poblacion():
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)
        lista = [int(fila[1]) for fila in leer]
        promedio = sum(lista) / len(lista)
        print(f"Promedio de población de {len(lista)} países: {promedio:.2f}")

#------- Promedio Superficie------#
def promedio_superficie():
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)
        lista = [int(fila[2]) for fila in leer]
        promedio = sum(lista) / len(lista)
        print(f"Promedio de superficie de {len(lista)} países: {promedio:.2f}")

#------- Cantidad de paises por continente -----#
def contar_por_continente():
    conteo = {}
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)
        for fila in leer:
            continente = fila[3].strip()
            if continente in conteo:
                conteo[continente] += 1
            else:
                conteo[continente] = 1
    for cont, cantidad in conteo.items():
        print(f"{cont}: {cantidad} países")

#------- Ordenar países -------#
def ordenar_paises(columna, descendente=False):
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        encabezado = next(leer)
        datos = list(leer)

    if columna in [1, 2]:
        datos.sort(key=lambda x: int(x[columna]),reverse=descendente) 
    else:  # nombre
        datos.sort(key=lambda x: x[columna].lower(),reverse=descendente)

    print(f"{'Nombre':15} | {'Población':>12} | {'Superficie':>12} | {'Continente'}")
    print("-" * 60)
    for fila in datos:
        print(f"{fila[0]:15} | {fila[1]:>12} | {fila[2]:>12} | {fila[3]}")

# ---------- MENÚ PRINCIPAL ----------- #
def menu_principal():
    opcion = 0
    while opcion != 5:
        print("""\n===== Menu Principal =====
1. Buscar país
2. Filtrar países 
3. Ordenar países 
4. Mostrar estadísticas 
5. Salir""")
        try:
            opcion = int(input("Elija una opción: "))
        except ValueError:
            print("❌ Opción no válida")
            continue

        # --- Buscar país ---
        if opcion == 1:
            buscar = input("Nombre de País: ")
            resultado = buscar_pais(buscar)
            if resultado:
                print("\n✅ Coincidencias:")
                for fila in resultado:
                    print(f"País: {fila[0]} | Población: {fila[1]} | Superficie: {fila[2]} | Continente: {fila[3]}")
            else:
                print(f"⚠️ No se encontraron países que empiecen con: {buscar!r}")

        # --- Filtrar ---
        elif opcion == 2:
            sub = 0
            while sub != 4:
                print("""\n===== Menu Filtrado =====
1. Continente
2. Rango Población
3. Rango Superficie
4. Volver""")
                try:
                    sub = int(input("Elija una opción: "))
                except ValueError:
                    print("❌ Solo números")
                    continue
                if sub == 1:
                    cont = input("Nombre de continente: ")
                    resultado = continentes(cont)
                    if resultado:
                        for f in resultado:
                            print(f"País: {f[0]} | Población: {f[1]} | Superficie: {f[2]} | Continente: {f[3]}")
                    else:
                        print("No se encontraron países.")
                elif sub == 2:
                    try:
                        minp = int(input("Mín Población: "))
                        maxp = int(input("Máx Población: "))
                        rango_poblacion(minp, maxp)
                    except ValueError:
                        print("❌ Solo números")
                elif sub == 3:
                    try:
                        mins = int(input("Mín Superficie: "))
                        maxs = int(input("Máx Superficie: "))
                        desc = input("Orden descendente? (s/n): ").lower() == "s"
                        rango_superficie(mins, maxs, desc)
                    except ValueError:
                        print("❌ Solo números")

        # --- Ordenar ---
        elif opcion == 3:
            sub = 0
            while sub != 4:
                print("""\n===== Ordenar países =====
1. Por nombre
2. Por población
3. Por superficie
4. Volver""")
                try:
                    sub = int(input("Elija una opción: "))
                except ValueError:
                    print("❌ Solo números")
                    continue
                if sub in [3]:
                    desc = input("Orden descendente? (s/n): ").lower() == "s"
                    ordenar_paises(sub-1,desc)
                elif sub in [1, 2]:
                    ordenar_paises(sub-1)

        # --- Estadísticas ---
        elif opcion == 4:
            sub = 0
            while sub != 5:
                print("""\n===== Estadísticas =====
1. Mayor y menor población
2. Promedio de población
3. Promedio de superficie
4. Cantidad de países por continente
5. Volver""")
                try:
                    sub = int(input("Elija una opción: "))
                except ValueError:
                    print("❌ Solo números")
                    continue
                if sub == 1:
                    mayor_menor_poblacion()
                elif sub == 2:
                    promedio_poblacion()
                elif sub == 3:
                    promedio_superficie()
                elif sub == 4:
                    contar_por_continente()
    else:
        print("GRACIAS POR VENIR..... NOS VEMOS PRONTO")
menu_principal()
