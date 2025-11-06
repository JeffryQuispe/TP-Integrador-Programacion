import csv
import os

CSV_FILE = "paises.csv"
CSV_HEADER = ["Nombre", "Poblacion", "Superficie", "Continente"]

# ---------- UTIL ----------- #
def asegurar_encabezado():
    """Crea el archivo CSV con encabezado si no existe o está vacío."""
    if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
        with open(CSV_FILE, "w", newline='', encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)

def leer_datos():
    """Devuelve lista de filas (sin encabezado)."""
    asegurar_encabezado()
    with open(CSV_FILE, newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer, None)
        return list(leer)

def escribir_todas_las_filas(filas):
    """Reescribe todo el CSV (incluye encabezado)."""
    with open(CSV_FILE, "w", newline='', encoding="utf-8-sig") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(CSV_HEADER)
        escritor.writerows(filas)

# ---------- FUNCIONES ----------- #

#------ Buscar ------------------#
def buscar_pais(prefijo):
    datos = leer_datos()
    encontrados = []
    for fila in datos:
        if fila[0].lower().startswith(prefijo.lower().strip()):
            encontrados.append(fila)
    return encontrados

#-------- Filtrado Paises  -------#
def continentes(continente):
    datos = leer_datos()
    resultado = []
    for fila in datos:
        if fila[3].lower().strip() == continente.lower().strip():
            resultado.append(fila)
    return resultado

# ------ Rango Población ------- #
def rango_poblacion(min_pob, max_pob):
    datos = leer_datos()
    for fila in datos:
        try:
            poblacion = int(fila[1])
        except (ValueError, IndexError):
            continue
        if min_pob <= poblacion <= max_pob:
            print(f"País: {fila[0]} - Población: {poblacion}")

#------- Rango Superficie -------#
def rango_superficie(min_sup, max_sup, descendente=False):
    datos = leer_datos()
    resultados = []
    for fila in datos:
        try:
            superficie = int(fila[2])
        except (ValueError, IndexError):
            continue
        if min_sup <= superficie <= max_sup:
            resultados.append((fila[0], superficie))
    resultados.sort(key=lambda x: x[1], reverse=descendente)
    for pais, sup in resultados:
        print(f"País: {pais} - Superficie: {sup}")

#------ Mayor y Menor Población -----#
def mayor_menor_poblacion():
    datos = leer_datos()
    max_pais = ("", 0)
    min_pais = ("", float('inf'))
    for fila in datos:
        try:
            poblacion = int(fila[1])
        except (ValueError, IndexError):
            continue
        if poblacion > max_pais[1]:
            max_pais = (fila[0], poblacion)
        if poblacion < min_pais[1]:
            min_pais = (fila[0], poblacion)
    if max_pais[0] == "":
        print("No hay datos de población.")
    else:
        print(f"🟢 Mayor población: {max_pais[0]} con {max_pais[1]}")
        print(f"🔴 Menor población: {min_pais[0]} con {min_pais[1]}")

#------- Promedio Población------#
def promedio_poblacion():
    datos = leer_datos()
    lista = []
    for fila in datos:
        try:
            lista.append(int(fila[1]))
        except (ValueError, IndexError):
            continue
    if not lista:
        print("No hay datos para calcular promedio de población.")
        return
    promedio = sum(lista) / len(lista)
    print(f"Promedio de población de {len(lista)} países: {promedio:.2f}")

#------- Promedio Superficie------#
def promedio_superficie():
    datos = leer_datos()
    lista = []
    for fila in datos:
        try:
            lista.append(int(fila[2]))
        except (ValueError, IndexError):
            continue
    if not lista:
        print("No hay datos para calcular promedio de superficie.")
        return
    promedio = sum(lista) / len(lista)
    print(f"Promedio de superficie de {len(lista)} países: {promedio:.2f}")

#------- Cantidad de paises por continente -----#
def contar_por_continente():
    datos = leer_datos()
    conteo = {}
    for fila in datos:
        continente = fila[3].strip() if len(fila) > 3 else ""
        conteo[continente] = conteo.get(continente, 0) + 1
    for cont, cantidad in conteo.items():
        print(f"{cont}: {cantidad} países")

#------- Ordenar países -------#
def ordenar_paises(columna, descendente=False):
    datos = leer_datos()
    # columna: 0=nombre,1=poblacion,2=superficie
    if columna in [1, 2]:
        datos.sort(key=lambda x: int(x[columna]) if len(x) > columna and x[columna].isdigit() else 0, reverse=descendente)
    else:
        datos.sort(key=lambda x: x[0].lower() if x else "", reverse=descendente)

    print(f"{'Nombre':20} | {'Población':>12} | {'Superficie':>12} | {'Continente'}")
    print("-" * 70)
    for fila in datos:
        nombre = fila[0] if len(fila) > 0 else ""
        pobl = fila[1] if len(fila) > 1 else ""
        sup = fila[2] if len(fila) > 2 else ""
        cont = fila[3] if len(fila) > 3 else ""
        print(f"{nombre:20} | {pobl:>12} | {sup:>12} | {cont}")

#------- Agregar país (mejorada, evita duplicados) -----#
def agregar_pais():
    asegurar_encabezado()
    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    # Verificar duplicado (comparación insensible a mayúsculas)
    datos = leer_datos()
    for fila in datos:
        if fila and fila[0].lower() == nombre.lower():
            print("⚠️ Ese país ya existe en la base de datos.")
            return
    try:
        poblacion = int(input("Población (número entero): ").strip())
        superficie = int(input("Superficie (km2, número entero): ").strip())
    except ValueError:
        print("❌ Población y superficie deben ser números enteros.")
        return
    continente = input("Continente: ").strip() or "Desconocido"

    print(f"\nVas a agregar: {nombre} | Población: {poblacion} | Superficie: {superficie} | Continente: {continente}")
    confirmar = input("Confirmar agregación? (s/n): ").lower()
    if confirmar != "s":
        print("Operación cancelada.")
        return

    with open(CSV_FILE, "a", newline='', encoding="utf-8-sig") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, str(poblacion), str(superficie), continente])
    print("✅ País agregado correctamente.")

#------- Actualizar población y superficie de un país -----#
def actualizar_pais():
    datos = leer_datos()
    if not datos:
        print("No hay países para actualizar.")
        return

    nombre = input("Nombre del país a actualizar (puede ser prefijo): ").strip()
    if not nombre:
        print("❌ Debe ingresar un nombre o prefijo.")
        return

    coincidencias = [fila for fila in datos if fila and fila[0].lower().startswith(nombre.lower())]
    if not coincidencias:
        print("⚠️ No se encontraron coincidencias.")
        return

    # Si hay varias coincidencias, listarlas y pedir elegir índice
    if len(coincidencias) > 1:
        print("\nSe encontraron varias coincidencias:")
        for i, f in enumerate(coincidencias, start=1):
            pobl = f[1] if len(f) > 1 else ""
            sup = f[2] if len(f) > 2 else ""
            cont = f[3] if len(f) > 3 else ""
            print(f"{i}. {f[0]} | Población: {pobl} | Superficie: {sup} | Continente: {cont}")
        try:
            idx = int(input("Elija el número del país a actualizar: "))
            if idx < 1 or idx > len(coincidencias):
                print("❌ Índice inválido.")
                return
            fila_seleccionada = coincidencias[idx-1]
        except ValueError:
            print("❌ Entrada inválida.")
            return
    else:
        fila_seleccionada = coincidencias[0]

    # Encontrar la fila real en 'datos' (puede haber múltiples iguales; tomamos la primera coincidencia exacta del nombre)
    for i, f in enumerate(datos):
        if f and f[0].lower() == fila_seleccionada[0].lower():
            indice_real = i
            break
    else:
        print("Error al localizar fila en los datos.")
        return

    # Mostrar valores actuales y pedir nuevos (enter para mantener)
    actual_pob = datos[indice_real][1] if len(datos[indice_real]) > 1 else ""
    actual_sup = datos[indice_real][2] if len(datos[indice_real]) > 2 else ""
    print(f"Valores actuales -> Población: {actual_pob} | Superficie: {actual_sup}")
    nuevo_pob = input("Nueva población (enter para mantener): ").strip()
    nuevo_sup = input("Nueva superficie (enter para mantener): ").strip()

    # Validar y aplicar
    if nuevo_pob:
        try:
            nuevo_pob_val = int(nuevo_pob)
            datos[indice_real][1] = str(nuevo_pob_val)
        except ValueError:
            print("❌ Población no válida. Operación cancelada.")
            return
    if nuevo_sup:
        try:
            nuevo_sup_val = int(nuevo_sup)
            datos[indice_real][2] = str(nuevo_sup_val)
        except ValueError:
            print("❌ Superficie no válida. Operación cancelada.")
            return

    escribir_todas_las_filas(datos)
    print("✅ País actualizado correctamente.")

# ---------- MENÚ PRINCIPAL ----------- #
def menu_principal():
    asegurar_encabezado()
    opcion = 0
    while opcion != 7:
        print("""\n===== Menu Principal =====
1. Buscar país
2. Filtrar países 
3. Ordenar países 
4. Mostrar estadísticas 
5. Agregar país
6. Actualizar país (población / superficie)
7. Salir""")
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
                if sub == 3:
                    desc = input("Orden descendente? (s/n): ").lower() == "s"
                    ordenar_paises(sub-1, desc)
                elif sub in [1, 2]:
                    # para nombre (col 0) y población (col 1)
                    # permitimos preguntar descendente para población también
                    if sub == 2:
                        desc = input("Orden descendente? (s/n): ").lower() == "s"
                        ordenar_paises(sub-1, desc)
                    else:
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

        # --- Agregar país ---
        elif opcion == 5:
            agregar_pais()

        # --- Actualizar país ---
        elif opcion == 6:
            actualizar_pais()

        elif opcion == 7:
            break
        else:
            print("❌ Opción no reconocida. Intente nuevamente.")

    print("GRACIAS POR VENIR..... NOS VEMOS PRONTO")

if __name__ == "__main__":
    menu_principal()
