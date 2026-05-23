import numpy as np
from scipy import stats


def construir_indicadores(df):
    df = df.copy()

    df["eficiencia_remocion_DBO_%"] = (
        (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"])
        / df["DBO_entrada_mg_L"]
    ) * 100

    df["eficiencia_remocion_DBO_%"] = df["eficiencia_remocion_DBO_%"].replace(
        [np.inf, -np.inf],
        np.nan
    )

    df["estado_cumplimiento"] = np.where(
        df["cumplimiento_norma"] == 1,
        "Cumple",
        "No cumple"
    )

    df["alerta_operativa"] = np.where(
        (df["cumplimiento_norma"] == 0) |
        (df["eficiencia_remocion_DBO_%"] < 70),
        "Alerta",
        "Normal"
    )

    return df


def detectar_valores_atipicos(df):
    df = df.copy()

    columnas_numericas = [
        "caudal_entrada_m3_d",
        "DBO_entrada_mg_L",
        "SST_entrada_mg_L",
        "pH_entrada",
        "energia_aeracion_kWh",
        "lodos_generados_kg_d",
        "DBO_salida_mg_L",
        "eficiencia_remocion_DBO_%"
    ]

    for columna in columnas_numericas:
        z_score = np.abs(stats.zscore(df[columna], nan_policy="omit"))
        df[f"anomalia_{columna}"] = np.where(z_score > 3, 1, 0)

    return df