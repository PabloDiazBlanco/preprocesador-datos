def seleccionar_columnas(df):
    """
    Permite al usuario seleccionar columnas de entrada (features) y salida (target).
    """
    print("\n=============================")
    print("Selección de Columnas")
    print("=============================")
    print("Columnas disponibles en los datos:")
    
    columnas = list(df.columns)
    for i, col in enumerate(columnas, 1):
        print(f"  [{i}] {col}")
    
    while True:
        try:
            features_idx = input("\nIngrese los números de las columnas de entrada (features), separados por comas: ")
            features_idx = [int(x.strip()) - 1 for x in features_idx.split(',')]
            features = [columnas[i] for i in features_idx]
            
            target_idx = int(input("\nIngrese el número de la columna de salida (target): ")) - 1
            target = columnas[target_idx]
            
            if target in features:
                print("⚠ Error: El target no puede estar en las features. Inténtelo de nuevo.\n")
                continue
            
            print(f"\nSelección guardada: Features = {features}, Target = '{target}'\n")
            return features, target
        except (ValueError, IndexError):
            print("⚠ Error: Entrada inválida. Asegúrese de ingresar números válidos y separados por comas. Inténtelo de nuevo.\n")
