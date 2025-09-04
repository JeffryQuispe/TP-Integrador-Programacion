import csv

# ------- Menú Principal -------- #
opcion = 0
while opcion != 5:
    print("""\n=== Menú Principal ===
    1 - Buscar País
    2 - Filtrado Países
    3 - Ordenado de Países
    4 - Estadísticas
    5 - Salir""")
    
    # Validar entrada del usuario
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("⚠️ Entrada inválida. Debe ingresar un número.")
        continue  # vuelve al menú principal
    
    # ------- Llamadas a funciones ------- #
    if opcion == 1:
        print("🔍 Buscar país (aquí iría la función)")
    
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

            # Submenú Continentes
            if sub == 1:
                print("🌍 Filtrar por continente \n")
                     
                while True:
                    print("""\n--- Continentes ---
                    1 - Volver al Menú Filtrado
                    2 - Salir del Programa""")
                    try:
                        sub_sub = int(input("Ingrese una opción: "))
                    except ValueError:
                        print("⚠️ Entrada inválida. Debe ingresar un número.")
                        continue
                    
                    if sub_sub == 1:
                        print("🔙 Volviendo al menú Filtrado...")
                        break  # Sale al Menú Filtrado
                    else:
                        print("⚠️ Opción no válida, intente de nuevo.")

            elif sub == 2:
                print("Filtrar por rango de población")
            elif sub == 3:
                print("Filtrar por rango de superficie")
            elif sub == 4:
                print("🔙 Volviendo al menú principal...")
            else:
                print("⚠️ Opción no válida, intente de nuevo.")
    
    elif opcion == 3:
        print("📊 Ordenar países (aquí iría la función)")
    
    elif opcion == 4:
        print("📈 Estadísticas (aquí iría la función)")
    
    elif opcion == 5:
        print("Gracias por usar el programa, hasta luego! 👋")
        break
    
    else:
        print("⚠️ Opción no válida, intente de nuevo.")
