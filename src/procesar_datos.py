import os
import numpy as np
import pandas as pd
from scipy import stats
import joblib

DATA_PATH = "data/dataset_set_A_aguas_residuales.xlsx"
OUTPUT_PATH = "outputs"

os.makedirs(OUTPUT_PATH, exist_ok=True)


def cargar_datos(ruta):
    df = pd.read_excel(ruta)
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce")
    return df


def evaluar_calidad_datos(df):
    resumen_calidad = pd.DataFrame({
        "columna": df.columns,
        "tipo_dato": df.dtypes.astype(str).values,
        "valores_nulos": df.isnull().sum().values,
        "porcentaje_nulos": (df.isnull().mean() * 100).round(2).values
    })

    duplicados = df.duplicated().sum()

    print("Resumen de calidad de datos:")
    print(resumen_calidad)
    print(f"\nCantidad de registros duplicados: {duplicados}")

    resumen_calidad.to_csv(f"{OUTPUT_PATH}/calidad_datos.csv", index=False)

    return resumen_calidad


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


def generar_archivos_salida(df):
    operaciones = df[
        [
            "fecha_registro",
            "planta",
            "caudal_entrada_m3_d",
            "DBO_entrada_mg_L",
            "DBO_salida_mg_L",
            "energia_aeracion_kWh",
            "lodos_generados_kg_d",
            "eficiencia_remocion_DBO_%",
            "alerta_operativa"
        ]
    ]

    gestion_ambiental = df[
        [
            "fecha_registro",
            "planta",
            "DBO_salida_mg_L",
            "cumplimiento_norma",
            "estado_cumplimiento"
        ]
    ]

    resumen = df.groupby("planta").agg(
        registros=("planta", "count"),
        caudal_promedio=("caudal_entrada_m3_d", "mean"),
        DBO_entrada_promedio=("DBO_entrada_mg_L", "mean"),
        DBO_salida_promedio=("DBO_salida_mg_L", "mean"),
        eficiencia_promedio=("eficiencia_remocion_DBO_%", "mean"),
        energia_promedio=("energia_aeracion_kWh", "mean"),
        lodos_promedio=("lodos_generados_kg_d", "mean"),
        tasa_cumplimiento=("cumplimiento_norma", "mean")
    ).reset_index()

    resumen["tasa_cumplimiento"] = (resumen["tasa_cumplimiento"] * 100).round(2)
    resumen["eficiencia_promedio"] = resumen["eficiencia_promedio"].round(2)

    operaciones.to_csv(f"{OUTPUT_PATH}/operaciones_aqualimpia.csv", index=False)
    gestion_ambiental.to_csv(f"{OUTPUT_PATH}/gestion_ambiental_aqualimpia.csv", index=False)
    resumen.to_csv(f"{OUTPUT_PATH}/resumen_indicadores.csv", index=False)

    joblib.dump(df, f"{OUTPUT_PATH}/dataset_procesado.joblib")

    return operaciones, gestion_ambiental, resumen


def main():
    df = cargar_datos(DATA_PATH)

    evaluar_calidad_datos(df)

    df = construir_indicadores(df)
    df = detectar_valores_atipicos(df)

    operaciones, gestion_ambiental, resumen = generar_archivos_salida(df)

    print("\nProceso finalizado correctamente.")
    print("\nResumen por planta:")
    print(resumen)


if __name__ == "__main__":
    main()