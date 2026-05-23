import pandas as pd


def cargar_datos(ruta):
    df = pd.read_excel(ruta)
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce")
    return df