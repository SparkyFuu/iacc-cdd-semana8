# Proyecto de Analisis de Datos - AquaLimpia S. A.

Este repositorio contiene un flujo modular de analisis de datos para evaluar el desempeno operativo y ambiental de plantas de tratamiento de aguas residuales de AquaLimpia S. A.

El proyecto permite cargar datos desde Excel, revisar calidad de datos, calcular indicadores, detectar valores atipicos, generar archivos de salida para distintas areas y visualizar los resultados en un dashboard interactivo desarrollado con Streamlit.

## Objetivos

- Analizar el comportamiento operativo y ambiental de las plantas de tratamiento.
- Calcular la eficiencia de remocion de DBO.
- Identificar registros con incumplimiento normativo.
- Generar alertas operativas para registros que requieren revision.
- Detectar posibles valores atipicos mediante z-score.
- Exportar archivos separados para Operaciones, Gestion Ambiental y resumen ejecutivo.
- Visualizar los indicadores principales en un dashboard interactivo.

## Estructura del proyecto

```text
aqualimpia-analisis/
|
|-- data/
|   |-- dataset_set_A_aguas_residuales.xlsx
|
|-- dashboard/
|   |-- dashboard_aqualimpia.py
|
|-- notebooks/
|   |-- analisis_aqualimpia.ipynb
|
|-- outputs/
|   |-- calidad_datos.csv
|   |-- operaciones_aqualimpia.csv
|   |-- gestion_ambiental_aqualimpia.csv
|   |-- resumen_indicadores.csv
|   |-- dataset_procesado.joblib
|
|-- src/
|   |-- procesamiento.py
|   |-- calidad_datos.py
|   |-- indicadores.py
|   |-- visualizaciones.py
|   |-- procesar_datos.py
|
|-- main.py
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## Diseno modular

El proyecto esta separado en modulos para que el codigo sea mas facil de entender, mantener y reutilizar:

- `main.py`: punto principal de ejecucion. Orquesta la carga, calidad de datos, indicadores, deteccion de anomalias y generacion de archivos.
- `src/procesamiento.py`: contiene la funcion de carga del dataset y conversion de fechas.
- `src/calidad_datos.py`: genera el resumen de calidad de datos, incluyendo tipos, nulos y duplicados.
- `src/indicadores.py`: calcula eficiencia de remocion de DBO, estado de cumplimiento, alertas operativas y anomalias.
- `src/visualizaciones.py`: contiene funciones auxiliares relacionadas con salidas del analisis.
- `dashboard/dashboard_aqualimpia.py`: aplicacion Streamlit para explorar los resultados visualmente.
- `notebooks/analisis_aqualimpia.ipynb`: notebook explicativo con el analisis paso a paso, graficos y conclusiones.

## Datos utilizados

El archivo de entrada esta en:

```text
data/dataset_set_A_aguas_residuales.xlsx
```

Incluye variables como:

- `fecha_registro`
- `planta`
- `caudal_entrada_m3_d`
- `DBO_entrada_mg_L`
- `SST_entrada_mg_L`
- `pH_entrada`
- `energia_aeracion_kWh`
- `lodos_generados_kg_d`
- `DBO_salida_mg_L`
- `cumplimiento_norma`

## Requisitos

Se recomienda usar Python 3.12 o una version compatible reciente.

Las dependencias del proyecto estan en `requirements.txt`:

```text
pandas
numpy
scipy
joblib
openpyxl
streamlit
plotly
```

## Instalacion paso a paso

Desde la carpeta del proyecto, crea y activa un entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
pip install -r requirements.txt
```

Si el entorno virtual tuvo instalaciones corruptas o errores de dependencias, se puede reinstalar encima con:

```powershell
pip install --ignore-installed -r requirements.txt
```

## Ejecucion del analisis

Para ejecutar el flujo completo:

```powershell
python main.py
```

Este comando realiza las siguientes acciones:

1. Carga el archivo Excel desde `data/`.
2. Convierte `fecha_registro` a formato fecha.
3. Evalua calidad de datos.
4. Calcula la eficiencia de remocion de DBO.
5. Clasifica el cumplimiento normativo.
6. Genera alertas operativas.
7. Detecta valores atipicos con z-score.
8. Exporta archivos CSV en `outputs/`.
9. Guarda `outputs/dataset_procesado.joblib`, usado por el dashboard.

Al finalizar, la consola muestra un resumen por planta.

## Archivos generados

El flujo principal genera estos archivos:

- `outputs/calidad_datos.csv`: resumen de tipos de datos, valores nulos y porcentaje de nulos.
- `outputs/operaciones_aqualimpia.csv`: archivo orientado a Operaciones, con caudal, DBO, energia, lodos, eficiencia y alerta operativa.
- `outputs/gestion_ambiental_aqualimpia.csv`: archivo orientado a Gestion Ambiental, con DBO de salida, cumplimiento y estado de cumplimiento.
- `outputs/resumen_indicadores.csv`: resumen por planta con indicadores promedio y tasa de cumplimiento.
- `outputs/dataset_procesado.joblib`: dataset procesado para uso interno del dashboard.

Nota: el archivo `.joblib` se genera localmente y esta ignorado por Git mediante `.gitignore`.

## Visualizacion con Streamlit

Antes de abrir el dashboard, ejecuta al menos una vez:

```powershell
python main.py
```

Esto asegura que exista `outputs/dataset_procesado.joblib`, que es el archivo que lee Streamlit.

Luego ejecuta:

```powershell
streamlit run dashboard/dashboard_aqualimpia.py
```

Streamlit mostrara una URL local similar a:

```text
Local URL: http://localhost:8501
```

Abre esa direccion en el navegador para visualizar el dashboard.

El dashboard permite:

- Filtrar por planta.
- Filtrar por rango de fechas.
- Ver total de registros analizados.
- Ver porcentaje de cumplimiento normativo.
- Ver DBO de salida promedio.
- Ver eficiencia promedio de remocion de DBO.
- Revisar la evolucion temporal de DBO de salida.
- Comparar cumplimiento por planta.
- Analizar relacion entre caudal de entrada y DBO de salida.
- Revisar energia de aireacion versus eficiencia.
- Consultar registros con alerta operativa.

## Notebook de analisis

El notebook esta en:

```text
notebooks/analisis_aqualimpia.ipynb
```

Contiene el analisis exploratorio documentado paso a paso:

- Carga de datos.
- Revision de calidad.
- Exploracion inicial.
- Construccion de indicadores.
- Resumen por planta.
- Graficos con Plotly.
- Deteccion de anomalias.
- Generacion de archivos de salida.
- Conclusiones del analisis.

Para abrirlo, usa Jupyter Notebook, JupyterLab o VS Code con soporte para notebooks.

Si necesitas instalar Jupyter en el entorno virtual:

```powershell
pip install jupyter
```

## Indicadores calculados

### Eficiencia de remocion de DBO

```text
Eficiencia DBO (%) = ((DBO entrada - DBO salida) / DBO entrada) * 100
```

### Estado de cumplimiento

Convierte `cumplimiento_norma` en una etiqueta legible:

```text
1 -> Cumple
0 -> No cumple
```

### Alerta operativa

Un registro queda marcado como `Alerta` si:

- No cumple la normativa, o
- Tiene eficiencia de remocion de DBO menor a 70%.

### Valores atipicos

Se aplica z-score sobre variables numericas relevantes. Si el valor absoluto del z-score es mayor que 3, se marca como anomalia.

## Resultados principales del analisis

Con el dataset actual se observaron estos resultados:

- 200 registros analizados.
- Periodo observado: 2025-07-01 a 2025-10-28.
- Tasa global de cumplimiento normativo: 22.50%.
- Eficiencia promedio de remocion de DBO: 87.09%.
- DBO de salida promedio: 36.18 mg/L.
- Registros con alerta operativa: 155.
- Planta Norte presenta la menor tasa de cumplimiento.
- Las anomalias detectadas se concentran principalmente en `lodos_generados_kg_d` y `DBO_salida_mg_L`.

## Flujo recomendado de trabajo

Cada vez que cambie el archivo de datos o se modifique la logica de indicadores:

```powershell
python main.py
streamlit run dashboard/dashboard_aqualimpia.py
```

Si se desea revisar o documentar el analisis con mas detalle, abrir y ejecutar:

```text
notebooks/analisis_aqualimpia.ipynb
```

## Conclusiones

El proyecto entrega una base reproducible para analizar el desempeno de AquaLimpia S. A. La separacion modular permite mantener el procesamiento, la calidad de datos, los indicadores y la visualizacion en componentes independientes.

Esto facilita extender el analisis, actualizar el dashboard, reutilizar funciones en notebooks y generar reportes consistentes para Operaciones y Gestion Ambiental.
