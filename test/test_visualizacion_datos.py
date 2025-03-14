import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
import pytest
from src.visualizacion_datos import resumen_estadistico

def test_resumen_estadistico(capsys):
    df = pd.DataFrame({
        'num': [1, 2, 3, 4],
        'cat': ['a', 'b', 'a', 'b']
    })
    resumen_estadistico(df, ['num', 'cat'])
    captured = capsys.readouterr().out
    # Verificar que se imprimen las estadísticas y la distribución de la variable categórica
    assert "mean" in captured
    assert "Distribución de la variable 'cat'" in captured
