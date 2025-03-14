import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import pandas as pd
import pytest
from src.normalizacion_escalado import normalizar_escalar

def test_normalizar_escalar_minmax(monkeypatch):
    df = pd.DataFrame({
        'num': [10, 20, 30],
        'cat': ['a', 'b', 'c']
    })
    # Simular opción "1" para Min-Max Scaling
    monkeypatch.setattr('builtins.input', lambda prompt: "1")
    df_result, status = normalizar_escalar(df, ['num'])
    # Verificar que los valores de la columna 'num' están en el rango [0, 1]
    assert df_result['num'].min() >= 0 and df_result['num'].max() <= 1
    assert status is True

def test_normalizar_escalar_zscore(monkeypatch):
    df = pd.DataFrame({
        'num': [10, 20, 30],
        'cat': ['a', 'b', 'c']
    })
    # Simular opción "2" para Z-score Normalization
    monkeypatch.setattr('builtins.input', lambda prompt: "2")
    df_result, status = normalizar_escalar(df, ['num'])
    mean_val = df_result['num'].mean()
    # Usar numpy.std con ddof=0 para obtener la desviación estándar poblacional
    std_val = np.std(df_result['num'], ddof=0)
    # Comprobamos que la media esté cerca de 0 y la desviación estándar sea 1
    assert abs(mean_val) < 1e-6
    assert abs(std_val - 1) < 1e-6
    assert status is True
