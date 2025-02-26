from src.carga_datos import cargar_datos
from src.seleccionar_columnas import seleccionar_columnas
from src.manejo_valores_faltantes import manejar_valores_faltantes

datos_cargados = None
features = None
target = None
valores_faltantes_gestionados = False

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
        if features and target:
            print("[-] 2. Preprocesado de datos")
            print("      [✓] 2.1 Selección de columnas (completado)")
            if valores_faltantes_gestionados:
                print("      [✓] 2.2 Manejo de datos faltantes (completado)")
                print("      [-] 2.3 Transformación de datos categóricos (pendiente)")
            else:
                print("      [-] 2.2 Manejo de datos faltantes (pendiente)")
                print("      [✗] 2.3 Transformación de datos categóricos (requiere manejo de valores faltantes)")
            print("      [✗] 2.4 Normalización y escalado (requiere transformación categórica)")
            print("      [✗] 2.5 Detección y manejo de valores atípicos (requiere normalización)")
        else:
            print("[-] 2. Preprocesado de datos (selección de columnas requerida)")
        print("[✗] 3. Visualización de datos (requiere preprocesado completo)")
        print("[✗] 4. Exportar datos (requiere preprocesado completo)")
    print("[✓] 5. Salir")

def main():
    global datos_cargados, features, target, valores_faltantes_gestionados
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            df = cargar_datos()
            if df is not None:
                datos_cargados = "datos.csv"  # Aquí se debe actualizar con el nombre real del archivo cargado
                print("\nDatos cargados correctamente en memoria. Puede continuar con el preprocesamiento.")
        elif opcion == "2" and datos_cargados:
            if not features or not target:
                features, target = seleccionar_columnas(df)
            elif not valores_faltantes_gestionados:
                df, valores_faltantes_gestionados = manejar_valores_faltantes(df, features, target)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida o función aún no disponible. Intente de nuevo.")

if __name__ == "__main__":
    main()
