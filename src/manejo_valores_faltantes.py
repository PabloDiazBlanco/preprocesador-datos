import pandas as pd

def manejar_valores_faltantes(df, features, target):
    """
    Gestiona los valores faltantes en las columnas seleccionadas, manejando correctamente datos mixtos.
    """
    columnas_seleccionadas = features + [target]
    valores_faltantes = df[columnas_seleccionadas].isnull().sum()
    valores_faltantes = valores_faltantes[valores_faltantes > 0]
    
    if valores_faltantes.empty:
        print("\n=============================")
        print("Manejo de Valores Faltantes")
        print("=============================")
        print("No se han detectado valores faltantes en las columnas seleccionadas.")
        print("No es necesario aplicar ninguna estrategia.")
        return df, True
    
    print("\n=============================")
    print("Manejo de Valores Faltantes")
    print("=============================")
    print("Se han detectado valores faltantes en las siguientes columnas seleccionadas:")
    for col, count in valores_faltantes.items():
        print(f"  - {col}: {count} valores faltantes")
    
    print("\nSeleccione una estrategia para manejar los valores faltantes:")
    print("  [1] Eliminar filas con valores faltantes")
    print("  [2] Rellenar con la media de la columna (solo columnas numéricas)")
    print("  [3] Rellenar con la mediana de la columna (solo columnas numéricas)")
    print("  [4] Rellenar con la moda de la columna")
    print("  [5] Rellenar con un valor constante")
    print("  [6] Volver al menú principal")
    
    # Filtrar columnas numéricas para aplicar media y mediana correctamente
    columnas_numericas = df[columnas_seleccionadas].select_dtypes(include=['number']).columns.tolist()
    
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            df = df.dropna(subset=columnas_seleccionadas)
            print("\nFilas con valores faltantes eliminadas.")
            break
        elif opcion == "2":
            if columnas_numericas:
                df[columnas_numericas] = df[columnas_numericas].apply(lambda col: col.fillna(col.mean()))
                print("\nValores faltantes rellenados con la media de cada columna numérica.")
            else:
                print("⚠ No hay columnas numéricas para aplicar la media.")
            break
        elif opcion == "3":
            if columnas_numericas:
                df[columnas_numericas] = df[columnas_numericas].apply(lambda col: col.fillna(col.median()))
                print("\nValores faltantes rellenados con la mediana de cada columna numérica.")
            else:
                print("⚠ No hay columnas numéricas para aplicar la mediana.")
            break
        elif opcion == "4":
            df[columnas_seleccionadas] = df[columnas_seleccionadas].apply(lambda col: col.fillna(col.mode()[0] if not col.mode().empty else col))
            print("\nValores faltantes rellenados con la moda de cada columna.")
            break
        elif opcion == "5":
            valor_constante = input("Seleccione un valor numérico para reemplazar los valores faltantes: ")
            df[columnas_seleccionadas] = df[columnas_seleccionadas].apply(lambda col: col.fillna(valor_constante))
            print(f"\nValores faltantes reemplazados con el valor {valor_constante}.")
            break
        elif opcion == "6":
            print("Volviendo al menú principal...")
            return df, False
        else:
            print("⚠ Error: Opción no válida. Intente de nuevo.")
    
    return df, True
