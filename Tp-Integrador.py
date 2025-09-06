import csv

from pywin.framework.interact import valueFormatOutputError

with open("paises.csv", newline='', encoding="utf-8-sig") as archivo:  # 👈 clave: utf-8-sig
    leer = csv.DictReader(archivo)
    for fila in leer:
        print(f"Pais: {fila['Nombre']} , Poblacion: {fila['Poblacion']} , Superficie: {fila['Superficie']} , Continente: {fila['Continente']}")

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
                    pass
                elif sub_menu == 3:
                    pass
                else:
                    print("🔙Volviendo al Menu Principal")

menu_princial()


