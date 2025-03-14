import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import os
import pandas as pd
import pytest
from src.exportar_datos import exportar_datos

def test_exportar_datos_csv(monkeypatch, tmp_path):
    df = pd.DataFrame({'A': [1, 2, 3]})
    # Simular la opción "1" para exportar a CSV y el nombre de archivo "test_export"
    inputs = iter(["1", "test_export"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    # Cambiar el directorio de trabajo temporalmente a tmp_path
    old_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        exportar_datos(df)
        export_file = tmp_path / "test_export.csv"
        assert export_file.exists()
        df_exported = pd.read_csv(export_file)
        pd.testing.assert_frame_equal(df, df_exported)
    finally:
        os.chdir(old_dir)

def test_exportar_datos_excel(monkeypatch, tmp_path):
    df = pd.DataFrame({'A': [1, 2, 3]})
    # Simular la opción "2" para exportar a Excel y el nombre "test_export_excel"
    inputs = iter(["2", "test_export_excel"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    old_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        exportar_datos(df)
        export_file = tmp_path / "test_export_excel.xlsx"
        assert export_file.exists()
        df_exported = pd.read_excel(export_file)
        pd.testing.assert_frame_equal(df, df_exported)
    finally:
        os.chdir(old_dir)
