import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
import pytest
from src.seleccionar_columnas import seleccionar_columnas

def test_seleccionar_columnas(monkeypatch):
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    # Simular la entrada del usuario:
    # Se seleccionan las columnas 1 y 2 para features y la columna 3 para target.
    inputs = iter(["1,2", "3"])
    monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
    
    features, target = seleccionar_columnas(df)
    assert features == ['A', 'B']
    assert target == 'C'

