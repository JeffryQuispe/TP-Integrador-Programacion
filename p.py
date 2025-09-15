import csv

import csv

def buscar_pais(prefijo, archivo_csv="paises.csv"):
    """Busca países cuyo nombre empiece con el prefijo indicado y devuelve diccionarios"""
    with open(archivo_csv, newline='', encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)  # ✅ Usa claves del encabezado
        encontrados = []
        for fila in lector:
            if fila["Nombre"].lower().startswith(prefijo.lower().strip()):
                encontrados.append({
                    "Nombre": fila["Nombre"],
                    "Poblacion": int(fila["poblacion"]),
                    "Superficie": int(fila["Superficie"]),
                    "Continente": fila["Continente"]
                })
        return encontrados

# --- Uso de la función ---
prefijo = input("Ingrese el inicio del nombre del país a buscar: ")
resultados = buscar_pais(prefijo)

if resultados:
    print("\nPaíses encontrados:")
    for pais in resultados:
        print(pais)
else:
    print("No se encontraron países con ese prefijo.")
