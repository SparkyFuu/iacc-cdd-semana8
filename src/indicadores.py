"""Calculo de indicadores para Aqualimpia."""

import pandas as pd


def calcular_resumen_numerico(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula estadisticos descriptivos para columnas numericas."""
    return df.describe(include="number").T.reset_index(names="indicador")
