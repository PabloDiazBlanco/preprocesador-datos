import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import sqlite3  # Agrega esta línea
import pytest
import pandas as pd
from src.carga_datos import cargar_csv, cargar_excel, cargar_sqlite, mostrar_info_dataset, seleccionar_tabla_sqlite

def test_cargar_csv(tmp_path):
    csv_content = "A,B,C\n1,2,3\n4,5,6\n"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content)
    
    df = cargar_csv(str(file_path))
    assert df is not None
    assert df.shape == (2, 3)
    assert list(df.columns) == ["A", "B", "C"]

def test_cargar_excel(tmp_path):
    df_original = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    file_path = tmp_path / "test.xlsx"
    df_original.to_excel(file_path, index=False)
    
    df = cargar_excel(str(file_path))
    assert df is not None
    assert df.shape == (2, 2)

def test_cargar_sqlite(tmp_path):
    # Crear una base de datos SQLite temporal con una tabla simple
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test (id INTEGER, value TEXT)")
    cursor.execute("INSERT INTO test VALUES (1, 'a'), (2, 'b')")
    conn.commit()
    conn.close()
    
    df = cargar_sqlite(str(db_path), "test")
    assert df is not None
    assert df.shape == (2, 2)
