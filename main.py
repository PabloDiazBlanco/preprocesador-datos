from src.carga_datos import cargar_datos
from src.seleccionar_columnas import seleccionar_columnas

datos_cargados = None
features = None
target = None

def mostrar_menu():
    print("\n=============================")
    print("Menú Principal")
    print("=============================")
    if datos_cargados is None:
        print("[-] 1. Cargar datos (ningún archivo cargado)")
        print("[✗] 2. Preprocesado de datos (requiere carga de datos)")
        print("[✗] 3. Visualización de datos (requiere preprocesado completo)")
        print("[✗] 4. Exportar datos (requiere preprocesado completo)")
    else:
        print(f"[✓] 1. Cargar datos (archivo: {datos_cargados})")
        if features and target:
            print("[-] 2. Preprocesado de datos")
            print("      [✓] 2.1 Selección de columnas (completado)")
            print("      [-] 2.2 Manejo de datos faltantes (pendiente)")
            print("      [✗] 2.3 Transformación de datos categóricos (pendiente)")
            print("      [✗] 2.4 Normalización y escalado (requiere transformación categórica)")
            print("      [✗] 2.5 Detección y manejo de valores atípicos (requiere normalización)")
        else:
            print("[-] 2. Preprocesado de datos (selección de columnas requerida)")
        print("[✗] 3. Visualización de datos (requiere preprocesado completo)")
        print("[✗] 4. Exportar datos (requiere preprocesado completo)")
    print("[✓] 5. Salir")

def main():
    global datos_cargados, features, target
    print("\n=================================")
    print("   Bienvenido al Pipeline CLI")
    print("=================================")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            df = cargar_datos()
            if df is not None:
                datos_cargados = "datos.csv"  # Aquí se debe actualizar con el nombre real del archivo cargado
                print("\nDatos cargados correctamente en memoria. Puede continuar con el preprocesamiento.")
        elif opcion == "2" and datos_cargados:
            features, target = seleccionar_columnas(df)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida o función aún no disponible. Intente de nuevo.")

if __name__ == "__main__":
    main()