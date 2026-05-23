# Proyecto de Análisis de Datos - AquaLimpia S. A.

## 1. Descripción del proyecto

Este proyecto tiene como objetivo analizar el desempeño de las plantas de tratamiento de aguas residuales de AquaLimpia S. A.

Durante el último trimestre se detectaron incumplimientos intermitentes en parámetros críticos, especialmente en la DBO de salida y en la eficiencia del tratamiento. Por eso, se desarrolló un análisis exploratorio que permite revisar el comportamiento de las plantas, detectar alertas operativas y apoyar la toma de decisiones de las áreas de Operaciones y Gestión Ambiental.

## 2. Objetivos

- Analizar el comportamiento operativo y ambiental de las plantas de tratamiento.
- Calcular la eficiencia de remoción de DBO.
- Identificar registros con incumplimiento normativo.
- Detectar posibles valores atípicos en variables relevantes.
- Generar archivos de salida para distintas áreas de la empresa.
- Construir un dashboard exploratorio para visualizar los principales resultados.

## 3. Estructura del proyecto

```text
aqualimpia-analisis/
│
├── data/
│   └── dataset_set_A_aguas_residuales.xlsx
│
├── notebooks/
│   └── analisis_aqualimpia.ipynb
│
├── src/
│   ├── procesamiento.py
│   ├── calidad_datos.py
│   ├── indicadores.py
│   └── visualizaciones.py
│
├── dashboard/
│   └── dashboard_aqualimpia.py
│
├── outputs/
│   ├── operaciones_aqualimpia.csv
│   ├── gestion_ambiental_aqualimpia.csv
│   └── resumen_indicadores.csv
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 4. Datos utilizados

El dataset utilizado corresponde al archivo:

```text
dataset_set_A_aguas_residuales.xlsx
```

Este archivo contiene registros asociados a distintas plantas de tratamiento, incluyendo variables como:

- Fecha de registro.
- Planta de tratamiento.
- Caudal de entrada.
- DBO de entrada.
- DBO de salida.
- Energía utilizada en aireación.
- Lodos generados.
- Cumplimiento normativo.

## 5. Proceso de análisis

El proceso se desarrolló en las siguientes etapas:

1. Carga del dataset original desde la carpeta `data`.
2. Conversión de la columna `fecha_registro` a formato de fecha.
3. Revisión de calidad de datos, considerando valores nulos, tipos de datos y duplicados.
4. Cálculo de la eficiencia de remoción de DBO.
5. Creación del estado de cumplimiento normativo.
6. Generación de alertas operativas.
7. Detección de valores atípicos mediante z-score.
8. Generación de archivos de salida.
9. Construcción del dashboard exploratorio.

## 6. Indicadores calculados

El principal indicador calculado fue la eficiencia de remoción de DBO:

```text
Eficiencia DBO (%) = ((DBO entrada - DBO salida) / DBO entrada) * 100
```

También se generaron dos variables de apoyo:

```text
estado_cumplimiento
```

Indica si el registro cumple o no cumple la normativa.

```text
alerta_operativa
```

Indica si el registro requiere atención, ya sea por incumplimiento normativo o por baja eficiencia del tratamiento.

## 7. Archivos generados

El proyecto genera los siguientes archivos en la carpeta `outputs`:

```text
operaciones_aqualimpia.csv
```

Archivo orientado al área de Operaciones. Incluye fecha, planta, caudal de entrada, DBO de entrada, DBO de salida, energía de aireación, lodos generados, eficiencia de remoción y alerta operativa.

```text
gestion_ambiental_aqualimpia.csv
```

Archivo orientado al área de Gestión Ambiental. Incluye fecha, planta, DBO de salida, cumplimiento normativo y estado de cumplimiento.

```text
resumen_indicadores.csv
```

Archivo resumen por planta, útil para comparar desempeño general entre plantas.

## 8. Dashboard exploratorio

El dashboard permite visualizar el comportamiento de las plantas mediante gráficos y métricas principales.

Incluye:

- Total de registros analizados.
- Porcentaje de cumplimiento normativo.
- DBO de salida promedio.
- Eficiencia promedio de remoción de DBO.
- Evolución de la DBO de salida.
- Comparación de cumplimiento por planta.
- Relación entre caudal de entrada y DBO de salida.
- Registros con alerta operativa.

## 9. Instalación de librerías

Para instalar las dependencias del proyecto se debe ejecutar:

```bash
pip install -r requirements.txt
```

## 10. Ejecución del análisis

Para procesar los datos se debe ejecutar:

```bash
python src/procesar_datos.py
```

Este comando genera los archivos de salida dentro de la carpeta `outputs`.

## 11. Ejecución del dashboard

Para abrir el dashboard se debe ejecutar:

```bash
streamlit run dashboard/dashboard_aqualimpia.py
```

Luego se abrirá una ventana en el navegador con la visualización del proyecto.

## 12. Resultados esperados

Con este proyecto se espera obtener una visión más clara del desempeño de las plantas de tratamiento. Los resultados permiten identificar plantas con menor eficiencia, registros con incumplimiento normativo y posibles situaciones operativas que requieren revisión.

El análisis también facilita la generación de evidencia para apoyar decisiones internas y reportes ambientales.

## 13. Conclusión

La documentación técnica permite que el proyecto sea más fácil de entender, ejecutar y mantener. En el caso de AquaLimpia S. A., esto es especialmente importante porque los resultados pueden ser usados por distintas áreas de la empresa y deben ser claros, trazables y reproducibles.
