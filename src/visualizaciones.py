import joblib


def guardar_dataset_procesado(df, output_path):
    joblib.dump(df, f"{output_path}/dataset_procesado.joblib")