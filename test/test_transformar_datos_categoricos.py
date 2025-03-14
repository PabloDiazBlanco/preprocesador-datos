import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
import pytest
from src.transformar_datos_categoricos import transformar_datos_categoricos

def test_transformar_datos_categoricos_label(monkeypatch):
    df = pd.DataFrame({
        'cat': ['a', 'b', 'a'],
        'num': [1, 2, 3]
    })
    # Simular opción "2": aplicar Label Encoding
    monkeypatch.setattr('builtins.input', lambda prompt: "2")
    df_result, status = transformar_datos_categoricos(df, ['cat', 'num'])
    # Verificar que la columna 'cat' ahora es de tipo numérico
    assert pd.api.types.is_numeric_dtype(df_result['cat'])
    assert status is True

def test_transformar_datos_categoricos_onehot(monkeypatch):
    df = pd.DataFrame({
        'cat': ['a', 'b', 'a'],
        'num': [1, 2, 3]
    })
    # Simular opción "1": aplicar One-Hot Encoding
    monkeypatch.setattr('builtins.input', lambda prompt: "1")
    df_result, status = transformar_datos_categoricos(df, ['cat', 'num'])
    # Verificar que la columna original 'cat' ha desaparecido y se han creado columnas nuevas con prefijo "cat_"
    assert 'cat' not in df_result.columns
    new_cols = [col for col in df_result.columns if col.startswith('cat_')]
    assert len(new_cols) > 0
    assert status is True
