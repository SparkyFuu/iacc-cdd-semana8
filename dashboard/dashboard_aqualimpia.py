import pandas as pd
import streamlit as st
import plotly.express as px
import joblib

st.set_page_config(
    page_title="Dashboard AquaLimpia",
    layout="wide"
)

st.title("Dashboard Exploratorio AquaLimpia S. A.")
st.write("Visualización del desempeño ambiental y operativo de las plantas de tratamiento.")

df = joblib.load("outputs/dataset_procesado.joblib")

plantas = sorted(df["planta"].unique())

plantas_seleccionadas = st.sidebar.multiselect(
    "Seleccionar plantas",
    plantas,
    default=plantas
)

df_filtrado = df[df["planta"].isin(plantas_seleccionadas)]

fecha_min = df_filtrado["fecha_registro"].min()
fecha_max = df_filtrado["fecha_registro"].max()

rango_fechas = st.sidebar.date_input(
    "Rango de fechas",
    value=(fecha_min, fecha_max)
)

if len(rango_fechas) == 2:
    fecha_inicio, fecha_fin = rango_fechas
    df_filtrado = df_filtrado[
        (df_filtrado["fecha_registro"] >= pd.to_datetime(fecha_inicio)) &
        (df_filtrado["fecha_registro"] <= pd.to_datetime(fecha_fin))
    ]

total_registros = len(df_filtrado)
tasa_cumplimiento = df_filtrado["cumplimiento_norma"].mean() * 100
dbo_salida_promedio = df_filtrado["DBO_salida_mg_L"].mean()
eficiencia_promedio = df_filtrado["eficiencia_remocion_DBO_%"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Registros analizados", f"{total_registros}")
col2.metric("Cumplimiento normativo", f"{tasa_cumplimiento:.2f}%")
col3.metric("DBO salida promedio", f"{dbo_salida_promedio:.2f} mg/L")
col4.metric("Eficiencia promedio DBO", f"{eficiencia_promedio:.2f}%")

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    fig = px.line(
        df_filtrado.sort_values("fecha_registro"),
        x="fecha_registro",
        y="DBO_salida_mg_L",
        color="planta",
        title="Evolución de la DBO de salida por planta"
    )
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    cumplimiento_planta = df_filtrado.groupby("planta", as_index=False)["cumplimiento_norma"].mean()
    cumplimiento_planta["cumplimiento_norma"] = cumplimiento_planta["cumplimiento_norma"] * 100

    fig = px.bar(
        cumplimiento_planta,
        x="planta",
        y="cumplimiento_norma",
        title="Porcentaje de cumplimiento normativo por planta",
        text="cumplimiento_norma"
    )
    st.plotly_chart(fig, use_container_width=True)

col_c, col_d = st.columns(2)

with col_c:
    fig = px.scatter(
        df_filtrado,
        x="caudal_entrada_m3_d",
        y="DBO_salida_mg_L",
        color="estado_cumplimiento",
        hover_data=["fecha_registro", "planta"],
        title="Caudal de entrada vs DBO de salida"
    )
    st.plotly_chart(fig, use_container_width=True)

with col_d:
    fig = px.scatter(
        df_filtrado,
        x="energia_aeracion_kWh",
        y="eficiencia_remocion_DBO_%",
        color="planta",
        hover_data=["fecha_registro", "estado_cumplimiento"],
        title="Energía de aireación vs eficiencia de remoción de DBO"
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Registros con alerta operativa")

alertas = df_filtrado[df_filtrado["alerta_operativa"] == "Alerta"]

st.dataframe(
    alertas[
        [
            "fecha_registro",
            "planta",
            "caudal_entrada_m3_d",
            "DBO_entrada_mg_L",
            "DBO_salida_mg_L",
            "eficiencia_remocion_DBO_%",
            "energia_aeracion_kWh",
            "lodos_generados_kg_d",
            "estado_cumplimiento"
        ]
    ],
    use_container_width=True
)