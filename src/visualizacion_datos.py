import pandas as pd
import matplotlib.pyplot as plt

def resumen_estadistico(df, features):
    """
    Muestra un resumen estadístico para variables numéricas y distribuciones para variables categóricas.
    """
    print("\nResumen estadístico de las variables seleccionadas:")
    print("--------------------------------------------------")
    numeric_feats = [col for col in features if col in df.columns and pd.api.types.is_numeric_dtype(df[col])]
    categorical_feats = [col for col in features if col in df.columns and not pd.api.types.is_numeric_dtype(df[col])]
    
    if numeric_feats:
        resumen = df[numeric_feats].describe().T
        # Añadimos la mediana que es el percentil 50
        resumen['median'] = df[numeric_feats].median()
        print("\nVariables numéricas:")
        print(resumen[['mean', 'median', 'std', 'min', 'max']])
    else:
        print("\nNo se han seleccionado variables numéricas.")
    
    if categorical_feats:
        print("\nVariables categóricas:")
        for col in categorical_feats:
            print(f"\nDistribución de la variable '{col}':")
            print(df[col].value_counts())
    else:
        print("\nNo se han seleccionado variables categóricas.")

def mostrar_histogramas(df, features):
    """
    Genera histogramas para las variables numéricas seleccionadas.
    """
    numeric_feats = [col for col in features if col in df.columns and pd.api.types.is_numeric_dtype(df[col])]
    if not numeric_feats:
        print("No se han seleccionado variables numéricas para generar histogramas.")
        return
    for col in numeric_feats:
        plt.figure()
        plt.hist(df[col].dropna(), bins=20, edgecolor='black')
        plt.title(f"Histograma de {col}")
        plt.xlabel(col)
        plt.ylabel("Frecuencia")
        plt.show()

def mostrar_scatter_comparativo(df_original, df_preprocesado, features):
    """
    Permite seleccionar una variable numérica y muestra un gráfico de dispersión comparando
    los valores originales versus los preprocesados.
    """
    numeric_feats = [col for col in features if col in df_original.columns and pd.api.types.is_numeric_dtype(df_original[col])]
    if not numeric_feats:
        print("No se han seleccionado variables numéricas para generar gráficos de dispersión.")
        return
    print("Variables numéricas disponibles para gráfico de dispersión:")
    for idx, col in enumerate(numeric_feats, 1):
        print(f"  [{idx}] {col}")
    try:
        opcion = int(input("Seleccione el número de la variable: "))
        if opcion < 1 or opcion > len(numeric_feats):
            print("Opción inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return
    col = numeric_feats[opcion - 1]
    plt.figure()
    plt.scatter(df_original[col], df_preprocesado[col], alpha=0.6)
    plt.title(f"Dispersión: {col} - Original vs Preprocesado")
    plt.xlabel("Original")
    plt.ylabel("Preprocesado")
    plt.show()

def mostrar_heatmap(df, features):
    """
    Genera un heatmap de correlación para las variables numéricas seleccionadas.
    """
    numeric_feats = [col for col in features if col in df.columns and pd.api.types.is_numeric_dtype(df[col])]
    if not numeric_feats:
        print("No se han seleccionado variables numéricas para generar un heatmap de correlación.")
        return
    corr = df[numeric_feats].corr()
    plt.figure()
    plt.imshow(corr, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.xticks(range(len(numeric_feats)), numeric_feats, rotation=90)
    plt.yticks(range(len(numeric_feats)), numeric_feats)
    plt.title("Heatmap de correlación")
    plt.tight_layout()
    plt.show()

def visualizar_datos(df_original, df_preprocesado, features):
    """
    Permite al usuario visualizar datos antes y después del preprocesamiento.
    """
    while True:
        print("\n=============================")
        print("Visualización de Datos")
        print("=============================")
        print("Seleccione qué tipo de visualización desea generar:")
        print("  [1] Resumen estadístico de las variables seleccionadas")
        print("  [2] Histogramas de variables numéricas")
        print("  [3] Gráficos de dispersión (Original vs Preprocesado)")
        print("  [4] Heatmap de correlación de variables numéricas")
        print("  [5] Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\nResumen estadístico (Original):")
            resumen_estadistico(df_original, features)
            print("\nResumen estadístico (Preprocesado):")
            resumen_estadistico(df_preprocesado, features)
        elif opcion == "2":
            print("\nHistogramas (Original):")
            mostrar_histogramas(df_original, features)
            print("\nHistogramas (Preprocesado):")
            mostrar_histogramas(df_preprocesado, features)
        elif opcion == "3":
            mostrar_scatter_comparativo(df_original, df_preprocesado, features)
        elif opcion == "4":
            mostrar_heatmap(df_preprocesado, features)
        elif opcion == "5":
            break
        else:
            print("⚠ Error: Opción no válida. Intente de nuevo.")
    return True
