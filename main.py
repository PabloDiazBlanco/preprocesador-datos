from src.carga_datos import cargar_datos
from src.seleccionar_columnas import seleccionar_columnas
from src.manejo_valores_faltantes import manejar_valores_faltantes
from src.transformar_datos_categoricos import transformar_datos_categoricos
from src.normalizacion_escalado import normalizar_escalar
from src.deteccion_valores_atipicos import gestionar_valores_atipicos
from src.visualizacion_datos import visualizar_datos

# Variables globales para el estado del pipeline
datos_cargados = None
features = None
target = None
valores_faltantes_gestionados = False
transformacion_categorica_realizada = False
normalizacion_escalado_realizado = False
deteccion_atipicos_realizada = False
visualizacion_completada = False  # Nuevo: estado de visualización

df_original = None  # Copia del dataset original para visualización

def preprocesamiento_completo():
    return (features and target and valores_faltantes_gestionados and
            transformacion_categorica_realizada and normalizacion_escalado_realizado and
            deteccion_atipicos_realizada)

# Menú principal (opciones generales)
def mostrar_menu():
    print("\n=============================")
    print("Menú Principal")
    print("=============================")
    if datos_cargados is None:
        print("[-] 1. Cargar datos (ningún archivo cargado)")
        print("[✗] 2. Preprocesado de datos (requiere carga de datos)")
        print("[✗] 3. Visualización de datos (requiere carga y preprocesado)")
        print("[✗] 4. Exportar datos (requiere carga y preprocesado)")
    else:
        print(f"[✓] 1. Cargar datos (archivo: {datos_cargados})")
        if preprocesamiento_completo():
            print("[✓] 2. Preprocesado de datos (completado)")
        else:
            print("[-] 2. Preprocesado de datos")
        # Para la visualización: si ya se completó, se muestra (completado)
        if visualizacion_completada:
            print("[✓] 3. Visualización de datos (completado)")
        else:
            # Solo se permite visualizar si el preprocesado está completo
            if preprocesamiento_completo():
                print("[✗] 3. Visualización de datos (pendiente)")
            else:
                print("[✗] 3. Visualización de datos (requiere preprocesado completo)")
        print("[✗] 4. Exportar datos (requiere preprocesado completo)")
    print("[✓] 5. Salir")

# Menú de preprocesado: muestra las subopciones 2.1 a 2.5 y su estado
def mostrar_menu_preprocesado():
    print("\n=============================")
    print("Menú Principal - Preprocesado")
    print("=============================")
    print("[✓] 1. Cargar datos (archivo: datos.csv)")
    print("[-] 2. Preprocesado de datos")
    
    # 2.1 Selección de columnas
    if features and target:
        print("      [✓] 2.1 Selección de columnas (completado)")
    else:
        print("      [-] 2.1 Selección de columnas (pendiente)")
    
    # 2.2 Manejo de valores faltantes
    if features and target:
        if valores_faltantes_gestionados:
            print("      [✓] 2.2 Manejo de valores faltantes (completado)")
        else:
            print("      [-] 2.2 Manejo de valores faltantes (pendiente)")
    else:
        print("      [✗] 2.2 Manejo de valores faltantes (requiere selección de columnas)")
    
    # 2.3 Transformación de datos categóricos
    if features and target and valores_faltantes_gestionados:
        if transformacion_categorica_realizada:
            print("      [✓] 2.3 Transformación de datos categóricos (completado)")
        else:
            print("      [-] 2.3 Transformación de datos categóricos (pendiente)")
    else:
        if not (features and target):
            print("      [✗] 2.3 Transformación de datos categóricos (requiere selección de columnas)")
        else:
            print("      [✗] 2.3 Transformación de datos categóricos (requiere manejo de valores faltantes)")
    
    # 2.4 Normalización y escalado
    if features and target and valores_faltantes_gestionados and transformacion_categorica_realizada:
        if normalizacion_escalado_realizado:
            print("      [✓] 2.4 Normalización y escalado (completado)")
        else:
            print("      [-] 2.4 Normalización y escalado (pendiente)")
    else:
        if not (features and target and transformacion_categorica_realizada):
            print("      [✗] 2.4 Normalización y escalado (requiere transformación categórica)")
        else:
            print("      [✗] 2.4 Normalización y escalado (pendiente)")
    
    # 2.5 Detección y manejo de valores atípicos
    if features and target and valores_faltantes_gestionados and transformacion_categorica_realizada and normalizacion_escalado_realizado:
        if deteccion_atipicos_realizada:
            print("      [✓] 2.5 Detección y manejo de valores atípicos (completado)")
        else:
            print("      [-] 2.5 Detección y manejo de valores atípicos (pendiente)")
    else:
        print("      [✗] 2.5 Detección y manejo de valores atípicos (requiere normalización)")
    
    print("[✗] 3. Visualización de datos (requiere preprocesado completo)")
    print("[✗] 4. Exportar datos (requiere preprocesado completo)")
    print("[✓] 5. Salir")

def main():
    global datos_cargados, features, target, valores_faltantes_gestionados
    global transformacion_categorica_realizada, normalizacion_escalado_realizado
    global deteccion_atipicos_realizada, visualizacion_completada, df_original
    df = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            df = cargar_datos()
            if df is not None:
                datos_cargados = "datos.csv"  # Se asume que el archivo es 'datos.csv'
                df_original = df.copy()  # Guardar copia original para visualización
                print("\n✔ Datos cargados correctamente en memoria. Puede continuar con el preprocesamiento.")

        elif opcion == "2" and datos_cargados:
            # Bucle para ejecutar las subopciones de preprocesado en orden
            while not preprocesamiento_completo():
                mostrar_menu_preprocesado()
                sub_opcion = input("Seleccione una opción de preprocesado (ej: 2.1, 2.2, etc.): ")
                if sub_opcion == "2.1":
                    features, target = seleccionar_columnas(df)
                elif sub_opcion == "2.2":
                    if features and target:
                        df, valores_faltantes_gestionados = manejar_valores_faltantes(df, features, target)
                    else:
                        print("⚠ Error: Primero debe seleccionar las columnas (2.1).")
                elif sub_opcion == "2.3":
                    if valores_faltantes_gestionados:
                        df, transformacion_categorica_realizada = transformar_datos_categoricos(df, features)
                    else:
                        print("⚠ Error: Primero debe manejar los valores faltantes (2.2).")
                elif sub_opcion == "2.4":
                    if transformacion_categorica_realizada:
                        df, normalizacion_escalado_realizado = normalizar_escalar(df, features)
                    else:
                        print("⚠ Error: Primero debe transformar los datos categóricos (2.3).")
                elif sub_opcion == "2.5":
                    if normalizacion_escalado_realizado:
                        df, deteccion_atipicos_realizada = gestionar_valores_atipicos(df, features)
                        print("\n✔ Preprocesamiento completado. Volviendo al menú principal...\n")
                    else:
                        print("⚠ Error: Primero debe normalizar y escalar los datos (2.4).")
                else:
                    print("⚠ Error: Opción no válida. Intente de nuevo.")

                if preprocesamiento_completo():
                    print("\n✔ ¡Preprocesamiento completado!\n")
                    break

        elif opcion == "3":
            if preprocesamiento_completo():
                visualizar_datos(df_original, df, features)
                visualizacion_completada = True
            else:
                print("⚠ No es posible visualizar los datos hasta que se complete el preprocesado.")

        elif opcion == "4":
            if preprocesamiento_completo():
                print("Funcionalidad de exportar datos no implementada aún.")
            else:
                print("⚠ No es posible exportar los datos hasta que se complete el preprocesado.")

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("⚠ Error: Opción no válida o función aún no disponible. Intente de nuevo.")

if __name__ == "__main__":
    main()
