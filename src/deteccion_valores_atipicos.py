import pandas as pd

def detectar_valores_atipicos(df, features):
    """
    Detecta outliers en las columnas numéricas seleccionadas usando el método IQR.
    Retorna un diccionario con el número de outliers por columna y la lista de columnas numéricas.
    """
    columnas_numericas = [col for col in features if col in df.columns and pd.api.types.is_numeric_dtype(df[col])]
    outliers_dict = {}
    for col in columnas_numericas:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        count = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
        if count > 0:
            outliers_dict[col] = count
    return outliers_dict, columnas_numericas

def gestionar_valores_atipicos(df, features):
    """
    Detecta y gestiona outliers en las columnas numéricas seleccionadas.
    Permite al usuario elegir entre:
      [1] Eliminar filas con outliers.
      [2] Reemplazar outliers con la mediana de la columna.
      [3] Mantener los outliers sin cambios.
      [4] Volver al menú principal.
    """
    print("\n=============================")
    print("Detección y Manejo de Valores Atípicos")
    print("=============================")
    
    outliers_dict, columnas_numericas = detectar_valores_atipicos(df, features)
    
    if not outliers_dict:
        print("No se han detectado valores atípicos en las columnas seleccionadas.")
        print("No es necesario aplicar ninguna estrategia.")
        return df, True
    
    print("Se han detectado valores atípicos en las siguientes columnas numéricas seleccionadas:")
    for col, count in outliers_dict.items():
        print(f"  - {col}: {count} valores atípicos detectados")
    
    print("\nSeleccione una estrategia para manejar los valores atípicos:")
    print("  [1] Eliminar filas con valores atípicos")
    print("  [2] Reemplazar valores atípicos con la mediana de la columna")
    print("  [3] Mantener valores atípicos sin cambios")
    print("  [4] Volver al menú principal")
    
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Crear máscara combinada para eliminar filas con al menos un outlier
            mask = pd.Series([False] * len(df))
            for col in outliers_dict.keys():
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                mask |= (df[col] < lower_bound) | (df[col] > upper_bound)
            df = df[~mask].reset_index(drop=True)
            print("\nFilas con valores atípicos eliminadas.")
            break
        elif opcion == "2":
            for col in outliers_dict.keys():
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                median_val = df[col].median()
                # Si la columna es de tipo entero, convertir la mediana a entero (redondeada)
                if pd.api.types.is_integer_dtype(df[col]):
                    median_val = int(round(median_val))
                df.loc[(df[col] < lower_bound) | (df[col] > upper_bound), col] = median_val
            print("\nValores atípicos reemplazados con la mediana de cada columna.")
            break
        elif opcion == "3":
            print("\nManteniendo los valores atípicos sin cambios.")
            break
        elif opcion == "4":
            print("Volviendo al menú principal...")
            return df, False
        else:
            print("⚠ Error: Opción no válida. Intente de nuevo.")
    
    return df, True
