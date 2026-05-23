import pandas as pd


def evaluar_calidad_datos(df, output_path):
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

    resumen_calidad.to_csv(f"{output_path}/calidad_datos.csv", index=False)

    return resumen_calidad