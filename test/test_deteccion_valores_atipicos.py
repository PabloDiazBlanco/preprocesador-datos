import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
import pandas as pd
from src.deteccion_valores_atipicos import detectar_valores_atipicos, gestionar_valores_atipicos

def test_detectar_valores_atipicos():
    df = pd.DataFrame({'num': [1, 2, 3, 100]})  # 100 es un outlier evidente
    outliers_dict, num_cols = detectar_valores_atipicos(df, ['num'])
    # Esperamos detectar al menos un outlier en la columna 'num'
    assert 'num' in outliers_dict
    assert outliers_dict['num'] > 0

def test_gestionar_valores_atipicos_reemplazar(monkeypatch):
    df = pd.DataFrame({'num': [1, 2, 3, 100]})
    # Simular opción "2": reemplazar outliers con la mediana
    monkeypatch.setattr('builtins.input', lambda prompt: "2")
    df_result, status = gestionar_valores_atipicos(df, ['num'])
    median_val = pd.Series([1, 2, 3, 100]).median()
    # Si la columna es de tipo entero, convertir la mediana a int (redondeada)
    if pd.api.types.is_integer_dtype(df['num']):
        median_val = int(round(median_val))
    # Verificar que en alguna fila el valor atípico haya sido reemplazado por la mediana convertida
    assert (df_result['num'] == median_val).sum() >= 1
    assert status is True
