import csv

from pywin.framework.interact import valueFormatOutputError

with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:  # 👈 clave: utf-8-sig
    leer = csv.DictReader(archivo)
    for fila in leer:
        print(f"Pais: {fila['Nombre']} , Poblacion: {fila['poblacion']} , Superficie: {fila['Superficie']} , Continente: {fila['Continente']}")

#-----------FUNCIONES------------#

#------ Buscar ------------------#

def buscar_pais (nombre):
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer) #salta la fila
        for fila in leer:
            if fila[0].lower() == nombre:
                return True
        return False

#-------- Filtrado Paises  -------#
def continentes (continente):
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
        next(leer)  # saltar encabezado

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
            superficie = int(fila[2])  # 👈 columna superficie
            if min_sup <= superficie <= max_sup:
                resultados.append((fila[0], superficie))  # (país, superficie)

    resultados.sort(key=lambda x: x[1], reverse=descendente)
    for pais, sup in resultados:
        print(f"País: {pais} - Superficie: {sup}")

#------ Mayor_Menor Población -----#
def mayor_menor_poblacion():
    with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:
        leer = csv.reader(archivo)
        next(leer)
        max_poblacion = []
        min_poblacion = []
        for fila in leer:
            poblacion = int(fila[1])
            max_poblacion.append(poblacion)
            min_poblacion.append(poblacion)
        print(f"El Pais con mas Población tiene {max(max_poblacion)} | y con menos población tiene {min(min_poblacion)}")




def menu_princial ():
    opcion = 0
    while opcion != 5:
        print("""===== Menu Principal =====
1. Buscar pais
2. Filtra Paises 
3. Ordenar Paises 
4. Mostrar Estadistica 
5. Salir """)
        try :
            opcion = int(input("Elija una Opcion: "))
        except ValueError:
            print("Opcion no valida")
            continue
        if opcion == 1:
            buscar = input("Nombre de Pais: ")
            resultado  = buscar_pais(buscar)
            if resultado:
                print(f"✅ Tu Pais fue encontrado :  {buscar}")
            else:
                print("⚠️Tu Pais no encontrado")
        if opcion == 2:
            sub_menu = 0
            while sub_menu != 4:
                print("""===== Menu Filtrado Paises =====
1. Continente
2. Rango Poblacion
3. Rango Superficie
4. Volver al Menu Principal""")
                try:
                    sub_menu = int(input("Elija una Opcion: "))
                except ValueError:
                    print("❌Opcion no valida,Solo Numero")
                    continue
                if sub_menu == 1:
                    buscar_continente = input("Nombre de Continente: ").lower()
                    resultado = continentes(buscar_continente)
                    if resultado:
                        print(f"Paises en contienete {buscar_continente}")
                        for resultados in resultado:
                            print(f"Pais : {resultados[0]} | Población : {resultados[1]} | Superficie : {resultados[2]} |Continente : {resultados[3]}")
                    else:
                        print("Continente no encontrado")
                elif sub_menu == 2:
                    try:
                        min_pob = int(input("Ingrese el Min Poblacion: "))
                        max_pob = int(input("Ingrese el Max Poblacion: "))
                        rango_poblacion(min_pob, max_pob)
                    except ValueError:
                        print("Opcion no valida,Solo Numero")
                elif sub_menu == 3:
                    try:
                        min_sup = int(input("Ingrese la superficie mínima: "))
                        max_sup = int(input("Ingrese la superficie máxima: "))
                        orden = input("Orden descendente? (s/n): ").lower() == "s"
                        rango_superficie(min_sup, max_sup, orden)
                    except ValueError:
                        print("⚠️ Debe ingresar números enteros.")
                else:
                    print("🔙Volviendo al Menu Principal")
        if opcion == 4:
            sub_menu = 0
            while sub_menu != 5:
                print("""===== Menu Filtrado Paises =====
1. Pais con Mayor y Menor Poblacion
2. Promedio de Población
3. Promedio de Superficie
4. Cantidad de paises por continente
5. volver al Menu Principal""")
                try:
                    sub_menu = int(input("Elija una Opcion: "))
                except ValueError:
                    print("Opcion no valida,Solo Numero")
                    continue
                if sub_menu == 1:
                    mayor_menor_poblacion()
                elif sub_menu == 2:
                    pass
                elif sub_menu == 3:
                    pass
                elif sub_menu == 4:
                    pass
                else:
                    print("🔙Volviendo al Menu Principal")

menu_princial()


