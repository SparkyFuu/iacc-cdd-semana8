"""Funciones de visualizacion para Aqualimpia."""

import pandas as pd
import plotly.express as px


def grafico_distribucion(df: pd.DataFrame, columna: str):
    """Crea un histograma para una columna numerica."""
    return px.histogram(df, x=columna, title=f"Distribucion de {columna}")
