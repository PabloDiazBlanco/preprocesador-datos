from src.carga_datos import cargar_datos
from src.seleccionar_columnas import seleccionar_columnas
from src.manejo_valores_faltantes import manejar_valores_faltantes
from src.transformar_datos_categoricos import transformar_datos_categoricos
from src.normalizacion_escalado import normalizar_escalar
from src.deteccion_valores_atipicos import gestionar_valores_atipicos

datos_cargados = None
features = None
target = None
valores_faltantes_gestionados = False
transformacion_categorica_realizada = False
normalizacion_escalado_realizado = False
deteccion_atipicos_realizada = False

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
        print("[-] 2. Preprocesado de datos")
        print("[✗] 3. Visualización de datos (requiere preprocesado completo)")
        print("[✗] 4. Exportar datos (requiere preprocesado completo)")
    print("[✓] 5. Salir")

def mostrar_menu_preprocesado():
    print("\n=============================")
    print("Menú Principal")
    print("=============================")
    print("[✓] 1. Cargar datos (archivo: datos.csv)")
    print("[-] 2. Preprocesado de datos")
    print("      [✓] 2.1 Selección de columnas (completado)" if features and target else "      [-] 2.1 Selección de columnas (pendiente)")
    if features and target:
        if valores_faltantes_gestionados:
            print("      [✓] 2.2 Manejo de valores faltantes (completado)")
            if transformacion_categorica_realizada:
                print("      [✓] 2.3 Transformación de datos categóricos (completado)")
                if normalizacion_escalado_realizado:
                    print("      [✓] 2.4 Normalización y escalado (completado)")
                else:
                    print("      [-] 2.4 Normalización y escalado (pendiente)")
            else:
                print("      [-] 2.3 Transformación de datos categóricos (pendiente)")
                print("      [✗] 2.4 Normalización y escalado (requiere transformación categórica)")
            if deteccion_atipicos_realizada:
                print("      [✓] 2.5 Detección y manejo de valores atípicos (completado)")
            else:
                print("      [-] 2.5 Detección y manejo de valores atípicos (pendiente)")
        else:
            print("      [-] 2.2 Manejo de valores faltantes (pendiente)")
            print("      [✗] 2.3 Transformación de datos categóricos (requiere manejo de valores faltantes)")
            print("      [✗] 2.4 Normalización y escalado (requiere transformación categórica)")
            print("      [✗] 2.5 Detección y manejo de valores atípicos (requiere normalización)")
    print("[✗] 3. Visualización de datos (requiere preprocesado completo)")
    print("[✗] 4. Exportar datos (requiere preprocesado completo)")
    print("[✓] 5. Salir")

def main():
    global datos_cargados, features, target, valores_faltantes_gestionados, transformacion_categorica_realizada, normalizacion_escalado_realizado, deteccion_atipicos_realizada
    df = None
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            df = cargar_datos()
            if df is not None:
                datos_cargados = "datos.csv"  # Actualizar con el nombre real del archivo cargado
                print("\nDatos cargados correctamente en memoria. Puede continuar con el preprocesamiento.")

        elif opcion == "2" and datos_cargados:
            while True:
                mostrar_menu_preprocesado()
                sub_opcion = input("Seleccione una opción de preprocesado (ejemplo: 2.1, 2.2, etc.): ")
                
                if sub_opcion == "2.1":
                    features, target = seleccionar_columnas(df)
                elif sub_opcion == "2.2" and features and target:
                    df, valores_faltantes_gestionados = manejar_valores_faltantes(df, features, target)
                elif sub_opcion == "2.3" and valores_faltantes_gestionados:
                    df, transformacion_categorica_realizada = transformar_datos_categoricos(df, features)
                elif sub_opcion == "2.4" and transformacion_categorica_realizada:
                    df, normalizacion_escalado_realizado = normalizar_escalar(df, features)
                elif sub_opcion == "2.5" and normalizacion_escalado_realizado:
                    df, deteccion_atipicos_realizada = gestionar_valores_atipicos(df, features)
                elif sub_opcion == "5":
                    print("Saliendo...")
                    return
                else:
                    print("⚠ Error: Opción no válida o requisito previo no cumplido. Intente de nuevo.")

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("⚠ Error: Opción no válida o función aún no disponible. Intente de nuevo.")

if __name__ == "__main__":
    main()
