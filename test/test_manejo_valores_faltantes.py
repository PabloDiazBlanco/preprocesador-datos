import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np  # Agrega esta línea
import pytest
import pandas as pd
from src.manejo_valores_faltantes import manejar_valores_faltantes

def test_manejar_valores_faltantes_eliminar(monkeypatch):
    df = pd.DataFrame({
        'A': [1, None, 3],
        'B': [4, 5, None],
        'C': [7, 8, 9]
    })
    # Simular opción "1": eliminar filas con valores faltantes
    monkeypatch.setattr('builtins.input', lambda prompt: "1")
    df_result, status = manejar_valores_faltantes(df, ['A', 'B'], 'C')
    # Verificar que las columnas A y B ya no contengan valores nulos
    assert df_result[['A', 'B']].isnull().sum().sum() == 0
    assert status is True

def test_manejar_valores_faltantes_media(monkeypatch):
    df = pd.DataFrame({
        'A': [1, np.nan, 3],
        'B': [4, 5, np.nan],
        'C': [7, 8, 9]
    })
    # Simular opción "2": rellenar con la media para columnas numéricas
    monkeypatch.setattr('builtins.input', lambda prompt: "2")
    df_result, status = manejar_valores_faltantes(df, ['A', 'B'], 'C')
    # Verificar que las columnas A y B ya no contengan valores NaN
    assert df_result[['A', 'B']].isnull().sum().sum() == 0
    assert status is True
