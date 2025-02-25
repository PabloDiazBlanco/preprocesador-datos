import pandas as pd
import sqlite3
import os

def cargar_csv(ruta):
    try:
        df = pd.read_csv(ruta, sep=None, engine='python')  # Detecta el separador automáticamente
        return df
    except Exception as e:
        print(f"Error al cargar CSV: {e}")
        return None

def cargar_excel(ruta):
    try:
        df = pd.read_excel(ruta)
        return df
    except Exception as e:
        print(f"Error al cargar Excel: {e}")
        return None

def cargar_sqlite(ruta, tabla):
    try:
        conexion = sqlite3.connect(ruta)
        df = pd.read_sql_query(f"SELECT * FROM {tabla}", conexion)
        conexion.close()
        return df
    except Exception as e:
        print(f"Error al cargar SQLite: {e}")
        return None

def mostrar_info_dataset(df):
    print("\nDatos cargados correctamente.")
    print(f"Número de filas: {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}")
    print("Tipos de datos:")
    print(df.dtypes)
    print("Primeras 5 filas:")
    print(df.head())

def seleccionar_tabla_sqlite(ruta):
    try:
        conexion = sqlite3.connect(ruta)
        cursor = conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas = cursor.fetchall()
        conexion.close()
        if not tablas:
            print("No se encontraron tablas en la base de datos.")
            return None
        print("Tablas disponibles:")
        for i, tabla in enumerate(tablas, 1):
            print(f"[{i}] {tabla[0]}")
        opcion = int(input("Seleccione una tabla: "))
        return tablas[opcion - 1][0] if 0 < opcion <= len(tablas) else None
    except Exception as e:
        print(f"Error al obtener tablas de SQLite: {e}")
        return None

def cargar_datos():
    print("\n=============================")
    print("Carga de Datos")
    print("=============================")
    print("Seleccione el tipo de archivo a cargar:")
    print("  [1] CSV")
    print("  [2] Excel")
    print("  [3] SQLite")
    print("  [4] Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        ruta = input("Ingrese la ruta del archivo CSV: ")
        if os.path.exists(ruta):
            df = cargar_csv(ruta)
            if df is not None:
                mostrar_info_dataset(df)
                return df
    elif opcion == "2":
        ruta = input("Ingrese la ruta del archivo Excel: ")
        if os.path.exists(ruta):
            df = cargar_excel(ruta)
            if df is not None:
                mostrar_info_dataset(df)
                return df
    elif opcion == "3":
        ruta = input("Ingrese la ruta de la base de datos SQLite: ")
        if os.path.exists(ruta):
            tabla = seleccionar_tabla_sqlite(ruta)
            if tabla:
                df = cargar_sqlite(ruta, tabla)
                if df is not None:
                    mostrar_info_dataset(df)
                    return df
    else:
        print("Volviendo al menú principal...")
        return None
    
    print("Error: No se pudo cargar el archivo. Asegúrese de que la ruta es correcta y el archivo es válido.")
    return None
