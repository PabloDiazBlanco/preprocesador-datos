import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def transformar_datos_categoricos(df, features):
    """
    Transforma las columnas categóricas seleccionadas en valores numéricos.
    """
    columnas_categoricas = [col for col in features if col in df.columns and df[col].dtype == 'object']
    
    print("\n=============================")
    print("Transformación de Datos Categóricos")
    print("=============================")
    
    if not columnas_categoricas:
        print("No se han detectado columnas categóricas en las variables de entrada seleccionadas.")
        print("No es necesario aplicar ninguna transformación.")
        return df, True
    
    print("Se han detectado columnas categóricas en las variables de entrada seleccionadas:")
    for col in columnas_categoricas:
        print(f"  - {col}")
    
    print("\nSeleccione una estrategia de transformación:")
    print("  [1] One-Hot Encoding (genera nuevas columnas binarias)")
    print("  [2] Label Encoding (convierte categorías a números enteros)")
    print("  [3] Volver al menú principal")
    
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            try:
                encoder = OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore')  
                df_encoded = pd.DataFrame(encoder.fit_transform(df[columnas_categoricas]))
                df_encoded.columns = encoder.get_feature_names_out(columnas_categoricas)
                df = df.drop(columns=columnas_categoricas).join(df_encoded)
                features = [col for col in features if col not in columnas_categoricas] + list(df_encoded.columns)
                print("\nTransformación completada con One-Hot Encoding.")
            except Exception as e:
                print(f"\n⚠ Error durante la transformación: {str(e)}")
            break
        elif opcion == "2":
            try:
                for col in columnas_categoricas:
                    encoder = LabelEncoder()
                    df[col] = encoder.fit_transform(df[col])
                print("\nTransformación completada con Label Encoding.")
            except Exception as e:
                print(f"\n⚠ Error durante la transformación: {str(e)}")
            break
        elif opcion == "3":
            print("Volviendo al menú principal...")
            return df, False
        else:
            print("⚠ Error: Opción no válida. Intente de nuevo.")
    
    return df, True
