"""Revision de calidad de datos para Aqualimpia."""

import pandas as pd


def resumen_calidad(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un resumen de valores nulos y tipos de datos."""
    return pd.DataFrame(
        {
            "columna": df.columns,
            "tipo_dato": [df[col].dtype for col in df.columns],
            "nulos": [df[col].isna().sum() for col in df.columns],
            "porcentaje_nulos": [df[col].isna().mean() * 100 for col in df.columns],
        }
    )
