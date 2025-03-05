import pandas as pd

def exportar_datos(df):
    """
    Exporta el DataFrame procesado a un archivo CSV o Excel (.xlsx).

    Permite al usuario seleccionar el formato de exportación y proporcionar un
    nombre de archivo (sin extensión). La función asume que el preprocesado y la
    visualización han sido completados, y se invoca únicamente en ese caso.
    """
    print("\n=============================")
    print("Exportación de Datos")
    print("=============================")
    print("Seleccione el formato de exportación:")
    print("  [1] CSV (.csv)")
    print("  [2] Excel (.xlsx)")
    print("  [3] Volver al menú principal")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        filename = input("Ingrese el nombre del archivo de salida (sin extensión): ")
        full_filename = f"{filename}.csv"
        try:
            df.to_csv(full_filename, index=False)
            print(f"Datos exportados correctamente como \"{full_filename}\".")
        except Exception as e:
            print(f"Error al exportar a CSV: {e}")
    elif opcion == "2":
        filename = input("Ingrese el nombre del archivo de salida (sin extensión): ")
        full_filename = f"{filename}.xlsx"
        try:
            df.to_excel(full_filename, index=False)
            print(f"Datos exportados correctamente como \"{full_filename}\".")
        except Exception as e:
            print(f"Error al exportar a Excel: {e}")
    elif opcion == "3":
        print("Volviendo al menú principal...")
    else:
        print("⚠ Error: Opción no válida. Intente de nuevo.")
