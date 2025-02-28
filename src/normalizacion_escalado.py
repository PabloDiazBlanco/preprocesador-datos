import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def normalizar_escalar(df, features):
    """
    Normaliza y escala las columnas numéricas seleccionadas dentro de las features.
    
    - Detecta las columnas numéricas dentro de las variables de entrada (features).
    - Muestra al usuario las columnas numéricas disponibles.
    - Permite elegir entre Min-Max Scaling o Z-score Normalization.
    - Si no hay columnas numéricas, informa al usuario y marca la transformación como completada.
    """
    # Filtrar solo las columnas que existen en df y que son numéricas
    columnas_numericas = [col for col in features if col in df.columns and pd.api.types.is_numeric_dtype(df[col])]
    
    print("\n=============================")
    print("Normalización y Escalado")
    print("=============================")
    
    if not columnas_numericas:
        print("No se han detectado columnas numéricas en las variables de entrada seleccionadas.")
        print("No es necesario aplicar ninguna normalización.")
        return df, True

    print("Se han detectado columnas numéricas en las variables de entrada seleccionadas:")
    for col in columnas_numericas:
        print(f"  - {col}")
    
    print("\nSeleccione una estrategia de normalización:")
    print("  [1] Min-Max Scaling (escala valores entre 0 y 1)")
    print("  [2] Z-score Normalization (media 0, desviación estándar 1)")
    print("  [3] Volver al menú principal")
    
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            try:
                scaler = MinMaxScaler()
                df_scaled = pd.DataFrame(scaler.fit_transform(df[columnas_numericas]), columns=columnas_numericas)
                # Asignación directa evitando df.update para no imprimir grandes arrays
                df[columnas_numericas] = df_scaled.astype(float)
                print("\nNormalización completada con Min-Max Scaling.")
            except Exception as e:
                print(f"\n⚠ Error durante la normalización con Min-Max Scaling: {str(e)}")
            break
        elif opcion == "2":
            try:
                scaler = StandardScaler()
                df_scaled = pd.DataFrame(scaler.fit_transform(df[columnas_numericas]), columns=columnas_numericas)
                df[columnas_numericas] = df_scaled.astype(float)
                print("\nNormalización completada con Z-score Normalization.")
            except Exception as e:
                print(f"\n⚠ Error durante la normalización con Z-score Normalization: {str(e)}")
            break
        elif opcion == "3":
            print("Volviendo al menú principal...")
            return df, False
        else:
            print("⚠ Error: Opción no válida. Intente de nuevo.")
    
    return df, True
